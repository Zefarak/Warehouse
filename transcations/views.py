from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from .models import *
from .forms import CreateBillForm, CreatePayrollForm

@method_decorator(staff_member_required, name='dispatch')
class BillingPaymentPage(TemplateView):
    template_name = 'billings/index.html'

    def get_context_data(self, **kwargs):
        context = super(BillingPaymentPage, self).get_context_data(**kwargs)
        billings = FixedCostInvoice.my_query.expiring_invoice()
        payroll = PayrollInvoice.my_query.not_paid().order_by('date_expired')
        context.update(locals())
        return context


@method_decorator(staff_member_required, name='dispatch')
class CreateBillPage(FormView):
    form_class = CreateBillForm
    template_name = 'dash_ware/form.html'

    def get_context_data(self, **kwargs):
        context = super(CreateBillPage, self).get_context_data(**kwargs)
        page_title = 'Add Billing Invoice'
        context.update(locals())
        return context

    def get_success_url(self):
        return reverse('billings:home')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class CreatePayrollPage(FormView):
    form_class = CreatePayrollForm
    template_name = 'dash_ware/form.html'

    def get_context_data(self, **kwargs):
        context = super(CreatePayrollPage, self).get_context_data(**kwargs)
        page_title = 'Add Payroll Invoice'
        context.update(locals())
        return context

    def get_success_url(self):
        return reverse('billings:home')




@method_decorator(staff_member_required, name='dispatch')
class BillingPage(ListView):
    model = FixedCostInvoice
    template_name = 'billings/billingsList.html'
    paginate_by= 20

    def get_context_data(self, **kwargs):
        context = super(BillingPage, self).get_context_data(**kwargs)
        categories = FixedCostsItem.objects.all()
        context.update(locals())
        return context


@method_decorator(staff_member_required, name='dispatch')
class BillingDetailPage(DetailView):
    model = FixedCostsItem
    template_name = ''

    def get_context_data(self, **kwargs):
        context = super(BillingDetailPage, self).get_context_data(**self)
        invoices = FixedCostInvoice.objects.filter(category=self.object)
        return context