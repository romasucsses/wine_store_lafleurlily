# Generated by Django 4.2.4 on 2023-11-03 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0007_alter_wine_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_generation', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupons', models.CharField(max_length=155)),
                ('date_expiration', models.DateField(verbose_name='%Y/%m/%d')),
                ('percent_discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=155)),
                ('last_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255)),
                ('street_address_1', models.TextField()),
                ('street_address_2', models.TextField(null=True)),
                ('city', models.CharField(max_length=155)),
                ('state', models.CharField(max_length=155)),
                ('zip_code', models.CharField(max_length=155)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('order_notes', models.TextField(default=None, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('cancel', 'Cancel'), ('delivered', 'Delivered')], default='pending', max_length=255)),
                ('cart_information', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='orders.cart')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cart_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.wine')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='orders.cartitem'),
        ),
    ]
