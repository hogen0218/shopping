# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-03 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_detail', '0002_item_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50, verbose_name='产品名称'),
        ),
    ]
