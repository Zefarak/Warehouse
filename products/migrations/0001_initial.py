# Generated by Django 2.0 on 2017-12-15 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import mptt.fields
import products.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True, verbose_name='Ονομασία Brand')),
                ('image', models.ImageField(blank=True, upload_to='brands/', verbose_name='Εικόνα')),
                ('order_by', models.IntegerField(default=1, verbose_name='Σειρά Προτεριότητας')),
                ('meta_keywords', models.CharField(blank=True, max_length=255)),
                ('meta_description', models.CharField(blank=True, max_length=255)),
                ('width', models.IntegerField(default=240)),
                ('height', models.IntegerField(default=240)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Ενεργοποίηση')),
            ],
            options={
                'verbose_name_plural': '4. Brands',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, unique=True, verbose_name='Τίτλος Κατηγορίας')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Περιγραφή')),
            ],
            options={
                'verbose_name': 'Κατηγορίες  ',
                'verbose_name_plural': 'Κατηγορία',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='CategorySite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('image', models.ImageField(blank=True, help_text='610*410', null=True, upload_to=products.models.category_site_directory_path)),
                ('content', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('a', 'active'), ('b', 'inactive')], default='a', max_length=1)),
                ('sort_order', models.IntegerField(default=1)),
                ('date_added', models.DateField(auto_now=True)),
                ('seo_keyword', models.CharField(blank=True, max_length=300)),
                ('meta_description', models.CharField(blank=True, max_length=300)),
                ('meta_keywords', models.CharField(blank=True, max_length=300)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.CategorySite')),
            ],
            options={
                'verbose_name_plural': '3. Κατηγορίες Site',
            },
            managers=[
                ('my_query', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ChangeQtyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Σχολιασμός')),
                ('day_added', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeQtyOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ChangeQtyOrder')),
            ],
        ),
        migrations.CreateModel(
            name='ChangeQtyOrderItemSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ChangeQtyOrder')),
            ],
        ),
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='CharacteristicsValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Ονομασία Χρώματος')),
                ('status', models.BooleanField(default=True, verbose_name='Κατάσταση')),
                ('code_id', models.CharField(blank=True, max_length=25, verbose_name='Κωδικός Χρώματος')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.Color')),
            ],
            options={
                'verbose_name_plural': '5. Χρώματα',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('site_active', models.BooleanField(default=True, verbose_name='Active for Site')),
                ('wholesale_active', models.BooleanField(default=False, verbose_name='Active for WholeSale')),
                ('is_service', models.BooleanField(default=False, verbose_name='Service')),
                ('size', models.BooleanField(default=False, verbose_name='Μεγεθολόγιο')),
                ('title', models.CharField(max_length=120, verbose_name="'Ονομα προιόντος")),
                ('order_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Κωδικός Τιμολογίου')),
                ('price_buy', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Αγοράς')),
                ('order_discount', models.IntegerField(default=0, verbose_name="'Εκπτωση Τιμολογίου σε %")),
                ('qty_kilo', models.DecimalField(decimal_places=3, default=1, max_digits=5, verbose_name='Βάρος/Τεμάχια ανά Συσκευασία ')),
                ('qty', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Απόθεμα')),
                ('barcode', models.CharField(blank=True, max_length=6, null=True, verbose_name='Κωδικός/Barcode')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Περιγραφή')),
                ('measure_unit', models.CharField(choices=[('1', 'Σε απόθεμα'), ('2', 'Inactive'), ('3', 'Διαθέσιμο με παραγγελία'), ('4', 'Προσωρινά μη διαθέσιμο')], max_length=1)),
                ('safe_stock', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('sku', models.CharField(blank=True, max_length=150, null=True)),
                ('site_text', tinymce.models.HTMLField(blank=True, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=300, null=True)),
                ('status', models.BooleanField(default=True, verbose_name='Κατάσταση Site')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή λιανικής')),
                ('margin', models.IntegerField(blank=True, default=30, null=True, verbose_name='Margin')),
                ('markup', models.IntegerField(blank=True, default=30, null=True, verbose_name='Markup')),
                ('price_internet', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Internet(No use)')),
                ('price_b2b', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Χονδρικής')),
                ('price_discount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Εκπτωτική Τιμή.')),
                ('final_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('day_added', models.DateField(default=django.utils.timezone.now, verbose_name='Ημερομηνία Δημιουργίας')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Brands', verbose_name='Brand Name')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
                ('category_site', models.ManyToManyField(to='products.CategorySite')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Color', verbose_name='Χρώμα')),
            ],
            options={
                'verbose_name_plural': '1. Προϊόντα',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ProductCharacteristics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('focus', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.CharacteristicsValue')),
                ('product_related', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Characteristics')),
            ],
            options={
                'verbose_name_plural': '9. Χαρακτηριστικά Προϊόντος',
            },
            managers=[
                ('my_query', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ProductPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('alt', models.CharField(blank=True, help_text='Θα δημιουργηθεί αυτόματα εάν δεν συμπληρωθεί', max_length=200, null=True)),
                ('title', models.CharField(blank=True, help_text='Θα δημιουργηθεί αυτόματα εάν δεν συμπληρωθεί', max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('is_primary', models.BooleanField(default=False, verbose_name='Αρχική Εικόνα')),
                ('is_back', models.BooleanField(default=False, verbose_name='Δεύτερη Εικόνα')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='RelatedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related', models.ManyToManyField(related_name='relatedgproducts', to='products.Product')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titleg', to='products.Product')),
            ],
            options={
                'verbose_name_plural': '7. Παρόμοια Προϊόντα',
            },
        ),
        migrations.CreateModel(
            name='SameColorProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related', models.ManyToManyField(related_name='relatedfproducts', to='products.Product')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titlef', to='products.Product')),
            ],
            options={
                'verbose_name_plural': '8. Ίδιο Χρώμα Προϊόντα',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Ονομασία Μεγέθους')),
                ('status', models.BooleanField(default=True, verbose_name='Κατάσταση')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.Size')),
            ],
            options={
                'verbose_name_plural': '6. Μεγέθη',
            },
        ),
        migrations.CreateModel(
            name='SizeAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order_discount', models.IntegerField(blank=True, default=0, null=True, verbose_name="'Εκπτωση Τιμολογίου σε %")),
                ('price_buy', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Αγοράς')),
                ('product_related', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Size')),
            ],
            options={
                'verbose_name_plural': '2. Μεγεθολόγιο',
            },
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, unique=True, verbose_name="'Ονομα")),
                ('afm', models.CharField(blank=True, max_length=9, null=True, verbose_name='ΑΦΜ')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, verbose_name='Τηλέφωνο')),
                ('phone1', models.CharField(blank=True, max_length=10, null=True, verbose_name='Τηλέφωνο')),
                ('fax', models.CharField(blank=True, max_length=10, null=True, verbose_name='Fax')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=100, verbose_name='Υπόλοιπο')),
                ('site', models.CharField(blank=True, max_length=40, null=True, verbose_name='Site')),
                ('address', models.CharField(blank=True, max_length=40, null=True, verbose_name='Διεύθυνση')),
                ('city', models.CharField(blank=True, max_length=40, null=True, verbose_name='Πόλη')),
                ('zip_code', models.CharField(blank=True, max_length=40, null=True, verbose_name='TK')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Περιγραφή')),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('taxes_modifier', models.IntegerField(default=24, verbose_name='ΦΠΑ Τιμολογίου.')),
                ('remaining_deposit', models.DecimalField(decimal_places=2, default=0, max_digits=100, verbose_name='Υπόλοιπο προκαταβολών')),
            ],
            options={
                'verbose_name_plural': '9. Προμηθευτές',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='TaxesCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'ΔΟΥ   ',
            },
        ),
        migrations.AddField(
            model_name='supply',
            name='doy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.TaxesCity', verbose_name='Εφορία'),
        ),
        migrations.AddField(
            model_name='product',
            name='supply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Supply', verbose_name='Προμηθευτής'),
        ),
        migrations.AddField(
            model_name='changeqtyorderitemsize',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.SizeAttribute'),
        ),
        migrations.AddField(
            model_name='changeqtyorderitem',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.SizeAttribute'),
        ),
        migrations.AddField(
            model_name='changeqtyorderitem',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='categorysite',
            unique_together={('slug', 'parent')},
        ),
    ]
