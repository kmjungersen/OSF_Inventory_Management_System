# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_auto_20150406_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationroom',
            old_name='room_id',
            new_name='location_id',
        ),
        migrations.RenameField(
            model_name='locationshelf',
            old_name='shelf_id',
            new_name='location_id',
        ),
        migrations.RenameField(
            model_name='locationunit',
            old_name='unit_id',
            new_name='location_id',
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 13, 21, 21, 21, 542110)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(verbose_name='date added', default=datetime.datetime(2015, 4, 14, 21, 21, 21, 541572)),
            preserve_default=True,
        ),
    ]
