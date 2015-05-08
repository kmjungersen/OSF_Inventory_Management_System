# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0022_auto_20150420_0429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationroom',
            old_name='location_id',
            new_name='room_id',
        ),
        migrations.RenameField(
            model_name='locationroom',
            old_name='name',
            new_name='room_name',
        ),
        migrations.RenameField(
            model_name='locationshelf',
            old_name='location_id',
            new_name='shelf_id',
        ),
        migrations.RenameField(
            model_name='locationunit',
            old_name='location_id',
            new_name='unit_id',
        ),
        migrations.RenameField(
            model_name='locationunit',
            old_name='temperature',
            new_name='unit_temperature',
        ),
        migrations.RenameField(
            model_name='locationunit',
            old_name='type',
            new_name='unit_type',
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 23, 20, 22, 49, 347042)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 20, 22, 49, 346505), verbose_name='date added'),
            preserve_default=True,
        ),
    ]
