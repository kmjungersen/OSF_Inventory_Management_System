# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20150318_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_number',
            field=models.BigIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(verbose_name='date added', default=datetime.datetime(2015, 3, 18, 19, 54, 52, 576639)),
            preserve_default=True,
        ),
    ]
