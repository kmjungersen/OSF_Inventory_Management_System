# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20150317_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_number',
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 18, 17, 19, 19, 650471), verbose_name='date added'),
            preserve_default=True,
        ),
    ]
