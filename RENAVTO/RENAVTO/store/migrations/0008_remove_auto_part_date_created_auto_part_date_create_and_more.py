# Generated by Django 4.0.6 on 2022-08-01 00:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_order_product_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto_part',
            name='date_created',
        ),
        migrations.AddField(
            model_name='auto_part',
            name='date_create',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Останній раз змінено:'),
        ),
        migrations.AddField(
            model_name='auto_part',
            name='produced_by',
            field=models.CharField(default=0, max_length=70, verbose_name='Виробник:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auto_part',
            name='car_brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.brand_of_car', verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='auto_part',
            name='car_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.model_of_car', verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='auto_part',
            name='part_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.part_category', verbose_name='Під тип'),
        ),
        migrations.AlterField(
            model_name='auto_part',
            name='part_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.type_of_part', verbose_name='Тип'),
        ),
    ]
