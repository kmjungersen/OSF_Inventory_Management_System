# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='item',
            name='cost',
            field=models.DecimalField(max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
    ]
