# Generated by Django 4.2.4 on 2023-09-17 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('stars_count', models.IntegerField()),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=355)),
                ('image', models.ImageField(upload_to='img/%Y/%m/%d/')),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=355)),
                ('description', models.TextField(null=True)),
                ('time_added', models.DateField(auto_now=True)),
                ('quanty', models.IntegerField()),
                ('slug', models.SlugField(max_length=455, unique=True, verbose_name='URL')),
                ('reviews', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.reviews')),
            ],
        ),
    ]