# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20150318_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='notes',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 18, 3, 7, 38, 374448)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(verbose_name='date added', default=datetime.datetime(2015, 3, 19, 3, 7, 38, 373829)),
            preserve_default=True,
        ),
    ]
