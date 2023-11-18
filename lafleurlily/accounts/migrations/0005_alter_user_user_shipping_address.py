# Generated by Django 4.2.4 on 2023-11-11 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_alter_checkoutaddress_user'),
        ('accounts', '0004_rename_orders_user_user_orders_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_shipping_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='orders.checkoutaddress'),
        ),
    ]