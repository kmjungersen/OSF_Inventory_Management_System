# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_auto_20150402_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='distributor',
            field=models.ForeignKey(to='inventory.Distributor', default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 5, 22, 27, 59, 873164)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(verbose_name='date added', default=datetime.datetime(2015, 4, 6, 22, 27, 59, 872627)),
            preserve_default=True,
        ),
    ]
