# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20150325_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='location_room',
        ),
        migrations.RemoveField(
            model_name='product',
            name='location_shelf',
        ),
        migrations.RemoveField(
            model_name='product',
            name='location_unit',
        ),
        migrations.AddField(
            model_name='item',
            name='location_room',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='location_shelf',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='location_unit',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 24, 0, 35, 8, 223434)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 0, 35, 8, 222940), verbose_name='date added'),
            preserve_default=True,
        ),
    ]
