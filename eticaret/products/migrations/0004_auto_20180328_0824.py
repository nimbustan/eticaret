# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-28 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180328_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='cateogory',
        ),
        migrations.AlterField(
            model_name='products',
            name='sub_cateogory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.SubCateogory'),
        ),
    ]
