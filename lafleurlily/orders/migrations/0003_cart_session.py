# Generated by Django 4.2.4 on 2023-11-04 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('orders', '0002_remove_cartitem_cart_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessions.session'),
        ),
    ]
