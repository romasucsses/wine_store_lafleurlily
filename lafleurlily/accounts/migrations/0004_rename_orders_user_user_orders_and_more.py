# Generated by Django 4.2.4 on 2023-11-11 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_checkoutaddress_user'),
        ('accounts', '0003_user_shipping_address_alter_user_orders_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='orders',
            new_name='user_orders',
        ),
        migrations.RemoveField(
            model_name='user',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='user',
            name='user_shipping_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='orders.checkoutaddress'),
        ),
    ]