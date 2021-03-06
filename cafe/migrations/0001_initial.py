# Generated by Django 2.1.7 on 2019-03-25 22:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sanat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanat_aty', models.CharField(default='Ыстық тамақтар', max_length=50, unique=True, verbose_name='санат атауы')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Уақыт')),
            ],
            options={
                'verbose_name': 'санат',
                'verbose_name_plural': 'санат',
            },
        ),
        migrations.CreateModel(
            name='SebetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameoo', models.CharField(blank=True, default='sebet', max_length=50, null=True, verbose_name='sebet')),
                ('product_sani', models.IntegerField(default=0, verbose_name='Sani')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sebet',
                'verbose_name_plural': 'Sebet',
            },
        ),
        migrations.CreateModel(
            name='Tamaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aty', models.CharField(max_length=50, unique=True, verbose_name='аты')),
                ('salmagi', models.IntegerField(default=0, verbose_name='салмағы')),
                ('baga', models.IntegerField(default=0, verbose_name='баға')),
                ('suret', models.ImageField(blank=True, upload_to='tamaq/%Y/%m/', verbose_name='сурет')),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('sanat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='санат', to='cafe.Sanat', verbose_name='санат')),
            ],
            options={
                'verbose_name': 'Tamaq',
                'verbose_name_plural': 'Tamaq',
            },
        ),
        migrations.AddField(
            model_name='sebetmodel',
            name='foods',
            field=models.ManyToManyField(blank=True, to='cafe.Tamaq', verbose_name='Tamaqtar'),
        ),
    ]
