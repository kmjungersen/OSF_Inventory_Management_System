# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20150319_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 18, 22, 39, 32, 134390)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 22, 39, 32, 133872), verbose_name='date added'),
            preserve_default=True,
        ),
    ]
