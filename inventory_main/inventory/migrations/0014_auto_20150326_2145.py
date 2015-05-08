# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20150325_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='checked_in',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 25, 21, 45, 0, 427195)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(verbose_name='date added', default=datetime.datetime(2015, 3, 26, 21, 45, 0, 426507)),
            preserve_default=True,
        ),
    ]
