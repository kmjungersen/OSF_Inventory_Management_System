# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20150318_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='lot_number',
            field=models.BigIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 17, 21, 11, 1, 620248)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_number',
            field=models.BigIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 18, 21, 11, 1, 619723), verbose_name='date added'),
            preserve_default=True,
        ),
    ]
