# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_auto_20150406_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='distributor',
            field=models.ForeignKey(null=True, to='inventory.Distributor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 5, 22, 30, 14, 549155)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 22, 30, 14, 548597), verbose_name='date added'),
            preserve_default=True,
        ),
    ]
