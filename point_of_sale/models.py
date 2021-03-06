from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import F,Sum


from django.utils import timezone
from account.models import CostumerAccount
from django.contrib import messages
from django.contrib.auth.models import User
import datetime
from model_utils import FieldTracker
from products.models import *
from inventory_manager.models import *
from dashboard.constants import *
from dashboard.models import Store, PaymentOrders, PaymentMethod
from dashboard.default_models import DefaultOrderModel, DefaultOrderItemModel
from cart.models import Cart, Coupons



def order_transcation(order_type, instance, qty, substact,): #  substact can be add or minus, change
    product = instance.title
    costumer = instance.order.costumer_account
    old_qty = instance.tracker.previous('qty')
    if order_type in ['e', 'r']:
        if substact == 'add':
            if old_qty:
                product.qty -= instance.qty - old_qty
            else:
                product.qty -= instance.qty
            if costumer:
                if old_qty:
                    costumer.balance -= old_qty * instance.final_price
                    costumer.balance += instance.get_total_value
                else:
                    costumer.balance += instance.get_total_value
        if substact == 'minus':
            product.qty += qty
            product.save()
            if costumer:
                if old_qty:
                    costumer.balance -= instance.get_total_value
    if order_type in ['d', 'b']:
        product.qty += instance.qty - old_qty if old_qty else instance.qty
        costumer.balance += old_qty*instance.final_price - instance.get_total_value if old_qty else -instance.get_total_value
    product.save()
    if costumer:
        costumer.save()


def payment_method_default():
    exists = PaymentMethod.objects.exists()
    return PaymentMethod.objects.first() if exists else None


#-------------------------Lianiki, epistrofes--------------------------------------------------------------------------------------


class ShippingManager(models.Manager):

    def active_and_site(self):
        return super(ShippingManager, self).filter(active=True, for_site=True)


class Shipping(models.Model):
    title = models.CharField(max_length=100,unique=True)
    content = models.CharField(max_length=300,default='Input here')
    active = models.BooleanField(default=True)
    ordering = models.IntegerField(default=1)
    for_site = models.BooleanField(default=True, verbose_name='Ενεργό για το Site')
    value = models.DecimalField(default=5, decimal_places=2, max_digits=5)
    value_limit = models.DecimalField(default=40, decimal_places=2, max_digits=5)
    objects = models.Manager()
    my_query = ShippingManager()

    class Meta:
        verbose_name_plural = 'Τρόποι Αποστολής'
        ordering = ['ordering', ]

    def __str__(self):
        return self.title

    def id_str(self):
        return str(self.id)

    def tag_value(self):
        return '%s %s' % (self.value, CURRENCY)

    def tag_value_limit(self):
        return '%s %s' % (self.value_limit, CURRENCY)


class RetailOrderManager(models.Manager):
    def all_orders_by_date_filter(self, date_start, date_end):
        return super(RetailOrderManager, self).filter(date_created__range=[date_start, date_end]).order_by('-date_created')

    def sells_orders(self, date_start, date_end):
        return self.all_orders_by_date_filter(date_start, date_end).filter(order_type__in=['r', 'e']).exclude(status__in=['5', '6'])

    def sellings_done(self):
        return super(RetailOrderManager, self).filter(status__id__in=[7,8]).exclude(order_type='b').order_by('-date_created')

    def sellings_not_done(self):
        return super(RetailOrderManager, self).exclude(status__id__in=[7,8], order_type='b')

    def eshop_orders(self):
        return super(RetailOrderManager, self).filter(order_type='e')

    def eshop_new_orders(self):
        return super(RetailOrderManager, self).filter(order_type='e', status_id=1).order_by('-id')

    def eshop_done_orders(self, date_start, date_end):
        return super(RetailOrderManager, self).filter(order_type__in=['e','r'], status__id=7, date_created__range=[date_start, date_end])

    def eshop_orders_on_progress(self):
        return super(RetailOrderManager, self).filter(order_type='e', status__id__in=[2, 3, 4, 5])

    def eshop_orders_in_warehouse(self):
        return super(RetailOrderManager, self).filter(order_type='e', status__id__in=[1, 2, 3, 4, 5])

    def retail_orders(self, date_start=None, date_end=None):
        if date_start and date_end:
            return super(RetailOrderManager, self).filter(order_type='r', date_created__range=[date_start, date_end]).order_by('-date_created')
        return super(RetailOrderManager, self).filter(order_type='r').order_by('-date_created')


class RetailOrderItemManager(models.Manager):
    def all_orders_by_date_filter(self, date_start, date_end):
        return super(RetailOrderItemManager, self).filter(order__date_created__range=[date_start, date_end])

    def selling_order_items(self, date_start, date_end):
        return super(RetailOrderItemManager, self).filter(order__order_type__in=['e', 'r'],
                                                          order__date_created__range=[date_start, date_end])

    def return_order_items(self, date_start, date_end):
        return super(RetailOrderItemManager ,self).filter(order__order_type='b',
                                                          order__date_created__range=[date_start, date_end])


class RetailOrder(DefaultOrderModel):
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default='1')
    order_type = models.CharField(max_length=1, choices=ORDER_TYPES, default='r')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                     verbose_name='Συνολικό Κόστος Παραγγελίας')
    costumer_account = models.ForeignKey(CostumerAccount, blank=True, null=True, verbose_name='Πελάτης', on_delete=models.CASCADE)
    #eshop info only

    shipping = models.ForeignKey(Shipping, null=True, blank=True, on_delete=models.CASCADE)
    shipping_cost = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    payment_cost = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    day_sent = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Όνομα')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Έπίθετο')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Πόλη')
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='Διεύθυνση')
    state = models.CharField(max_length=100, null=True, blank=True, verbose_name='Νομός')
    zip_code = models.IntegerField(null=True, blank=True, verbose_name='ΤΚ')
    cellphone = models.CharField(null=True, blank=True, verbose_name='Κινητό', max_length=10)
    phone = models.CharField(null=True, blank=True, verbose_name='Σταθερό Τηλεφωνο', max_length=10)
    email = models.EmailField(null=True, blank=True, )
    costumer_submit = models.BooleanField(default=True, verbose_name='Επιβεβαίωση')
    eshop_order_id = models.CharField(max_length=10, blank=True, null=True)
    eshop_session_id = models.CharField(max_length=50, blank=True, null=True)
    printed = models.BooleanField(default=False)

    my_query = RetailOrderManager()
    objects = models.Manager()

    cart_related = models.OneToOneField(Cart, blank=True, null=True, on_delete=models.SET_NULL)
    coupons = models.ManyToManyField(Coupons, blank=True)
    order_related = models.ForeignKey('self', blank=True, null=True, on_delete = models.CASCADE)
    payorders = GenericRelation(PaymentOrders)

    class Meta:
        verbose_name_plural = '1. Παραστατικά Πωλήσεων'

    def __str__(self):
        return self.title if self.title else 'order'

    def check_coupons(self):
        total_value = 0
        active_coupons = Coupons.my_query.active_date(date=datetime.datetime.now())
        for coupon in self.coupons.all():
            if coupon in active_coupons :
                if self.value > coupon.cart_total_value:
                    total_value += coupon.discount_value if coupon.discount_value else \
                    (coupon.discount_percent/100)*self.value if coupon.discount_percent else 0
        self.discount = total_value

    def save(self, *args, **kwargs):
        get_all_items = self.retailorderitem_set.all().values('cost', 'final_price', 'qty')
        self.count_items = get_all_items.count()
        self.value = get_all_items.aggregate(total=Sum(F('qty') * F('final_price')))['total'] if get_all_items else 0
        self.total_cost = get_all_items.aggregate(total=Sum(F('qty') * F('cost')))['total'] if get_all_items else 0
        try:
            self.check_coupons()
        except:
            self.discount = 0
        self.status = self.status if not self.is_paid else '7'
        self.final_price = self.shipping_cost + self.payment_cost + self.value - self.discount
        self.paid_value = self.payorders.aggregate(Sum('value'))['value__sum'] if self.payorders else 0
        self.paid_value = self.paid_value if self.paid_value else 0
        if self.status == '7':
            self.is_paid = True
        if self.is_paid and self.paid_value < self.final_price and not self.order_type == 'd':
            new_order = PaymentOrders.objects.create(payment_type=self.payment_method,
                                                     value=self.final_price - self.paid_value,
                                                     is_paid=True,
                                                     content_type=ContentType.objects.get_for_model(RetailOrder),
                                                     object_id=self.id,
                                                     date_expired=datetime.datetime.now(),
                                                     is_expense=False,
                                                     )
            self.paid_value += new_order.value
        super(RetailOrder, self).save(*args, **kwargs)
        if self.costumer_account:
            self.costumer_account.save()
        if self.order_type in ['b', 'd']:
            self.payorders.all().update(is_expense=True)

    def is_sale(self):
        return True if self.order_type in ['r', 'e'] else False

    def tag_value(self):
        return '%s %s' % (self.value, CURRENCY)

    def tag_final_price(self):
        return '%s %s' % (self.final_price, CURRENCY)
    tag_final_price.short_description = 'Τελική Αξία'

    def tag_paid_value(self):
        return '%s %s' % (self.paid_value, CURRENCY)
    tag_paid_value.short_description = 'Αποπληρωμένο Πόσο'

    def tag_cost_value(self):
        return '%s %s' % (self.total_cost, CURRENCY)

    def tag_discount(self):
        return '%s %s' %(self.discount, CURRENCY)

    @property
    def get_total_taxes(self):
        choice = 24
        for ele in TAXES_CHOICES:
            if ele[0] == self.taxes:
                choice = ele[1]
        return self.final_price * (Decimal(choice)/100)

    def tag_total_taxes(self):
        return '%s %s' % (self.get_total_taxes, CURRENCY)

    def tag_clean_value(self):
        return '%s %s' % (self.final_price - self.get_total_taxes, CURRENCY)

    def tag_shipping_value(self):
        return '%s %s' % (self.shipping_cost, CURRENCY)

    def tag_payment_value(self):
        return '%s %s' % (self.payment_cost, CURRENCY)

    @property
    def date_expired(self):
        return self.date_created

    @property
    def get_order_items(self):
        return self.retailorderitem_set.all()

    @property
    def tag_remain_value(self):
        return '%s %s' % (round(self.final_price - self.paid_value, 2), CURRENCY)

    def is_printed(self):
        return 'Printed' if self.printed else 'Not Printed'
    
    def tag_phones(self):
        return 'CellPhone.. %s, Phone %s' % (self.cellphone, self.phone) if self.phone else self.cellphone

    def tag_fullname(self):
        if self.costumer_account:
            return f'{self.first_name} {self.last_name}, Account: {self.costumer_account.user.username}'
        return f'{self.first_name} {self.last_name}'
    
    def tag_full_address(self):
        return f'{self.address}, City: {self.city}'

    @staticmethod
    def eshop_orders_filtering(request, queryset):
        search_name=request.GET.get('search_name', None)
        paid_name=request.GET.getlist('paid_name', None)
        printed_name=request.GET.get('printed_name', None)
        status_name=request.GET.getlist('status_name', None)
        payment_name=request.GET.getlist('payment_name', None)
        queryset = queryset.filter(printed=False) if printed_name else queryset
        queryset = queryset.filter(payment_method__id__in=payment_name) if payment_name else queryset
        queryset = queryset.filter(status__in=status_name) if status_name else queryset
        queryset = queryset.filter(is_paid=False) if paid_name else queryset
        queryset = queryset.filter(Q(title__icontains=search_name) |
                                   Q(cellphone__icontains=search_name) |
                                   Q(address__icontains=search_name) |
                                   Q(city__icontains=search_name) |
                                   Q(zip_code__icontains=search_name) |
                                   Q(phone__icontains=search_name) |
                                   Q(first_name__icontains=search_name) |
                                   Q(last_name__icontains=search_name)
                                   ).distinct() if search_name else queryset
        
        return queryset

    @staticmethod
    def estimate_shipping_and_payment_cost(order_value, shipping, payment):
        shipping_cost = shipping.value if shipping.value_limit < order_value else 0
        payment_cost = payment.additional_cost if payment.limit_value < order_value else 0
        return [shipping_cost, payment_cost]


@receiver(post_delete, sender=RetailOrder)
def update_on_delete_retail_order(sender, instance, *args, **kwargs):
    payments_order = instance.payorders.all()
    for order in payments_order:
        order.delete()
    order_items = instance.get_order_items
    for order in order_items:
        order.delete()


class RetailOrderItem(DefaultOrderItemModel):
    order = models.ForeignKey(RetailOrder, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    #  warehouse_management
    is_find = models.BooleanField(default=False)
    is_return = models.BooleanField(default=False)
    tracker = FieldTracker()

    my_query = RetailOrderItemManager()
    objects = models.Manager()

    class Meta:
        verbose_name_plural = '2. Προϊόντα Πωληθέντα'

    def __str__(self):
        return self.title.title

    def save(self, *args, **kwargs):
        if self.order.order_type in ['r', 'b', 'b', 'e']:
            self.price = self.title.price
            self.discount = self.title.price_discount
            self.cost = 0
            self.final_price = self.discount if self.discount > 0 else self.price
        else:
            self.price = 0
            self.discount = 0
            self.final_price = 0
            self.cost = 0
            self.final_price = 0
        super(RetailOrderItem, self).save(*args, **kwargs)
        self.order.save()
        self.title.save()

    def get_clean_value(self):
        return self.price * (100-self.order.taxes/100) * (100-Decimal(self.discount)/100)

    @property
    def get_total_value(self):
        return round(self.final_price*self.qty, 2)

    @property
    def get_total_cost_value(self):
        return round(self.cost * self.qty, 2)

    def tag_clean_value(self):
        return '%s %s' % (self.get_clean_value(), CURRENCY)

    def tag_total_price(self):
        return '%s %s' % (self.get_total_value, CURRENCY)
    tag_total_price.short_description = 'Συνολική Αξία'

    def tag_final_price(self):
        return '%s %s' % (self.final_price, CURRENCY)
    tag_final_price.short_description = 'Αξία Μονάδας'

    def tag_price(self):
        return '%s %s' % (self.price, CURRENCY)

    def tag_total_taxes(self):
        return '%s %s' %(round(self.price*self.qty*(Decimal(self.order.taxes)/100), 2), CURRENCY)

    def type_of_order(self):
        return self.order.order_type

    def template_tag_total_price(self):
        return "{0:.2f}".format(round(self.price*self.qty,2)) + ' %s'%(CURRENCY)

    def price_for_vendor_page(self):
        #returns silimar def for price in vendor_id page
        return self.price

    def absolute_url_vendor_page(self):
        return reverse('retail_order_section', kwargs={'dk': self.order.id})

    @staticmethod
    def check_if_exists(order, product):
        exists = RetailOrderItem.objects.filter(title=product, order=order)
        return exists.first() if exists else None


@receiver(post_delete, sender=RetailOrderItem)
def update_order_on_delete(sender, instance, *args, **kwargs):
    order = instance.order
    get_all_items = RetailOrderItem.objects.filter(order=order).values('cost', 'final_price', 'qty')
    order.count_items = get_all_items.count()
    order.value -= instance.get_total_value
    order.total_cost -= instance.get_total_cost_value
    order.save()
    if QTY_TRANSACTIONS:
        order_transcation(order_type=order.order_type, instance=instance, qty=instance.qty, substact='minus')
    instance.title.save()


@receiver(post_save, sender=RetailOrderItem)
def update_product_qty(sender, instance, *args, **kwargs):
    order_transcation(instance.order.order_type, instance, instance.qty, 'add')


def create_destroy_title():
    last_order = RetailOrderItem.objects.all().last()
    if last_order:
        number = int(last_order.id)+1
        return 'ΚΑΤ'+ str(number)
    else:
        return 'ΚΑΤ1'