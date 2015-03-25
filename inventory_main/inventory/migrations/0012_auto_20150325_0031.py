# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20150319_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location_room',
            field=models.CharField(null=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='location_shelf',
            field=models.CharField(null=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='location_unit',
            field=models.CharField(null=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 24, 0, 31, 9, 213122)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 0, 31, 9, 212386), verbose_name='date added'),
            preserve_default=True,
        ),
    ]
