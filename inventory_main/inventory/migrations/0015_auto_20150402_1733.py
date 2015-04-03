# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20150326_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('supplier_notes', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 1, 17, 33, 45, 257565)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(verbose_name='date added', default=datetime.datetime(2015, 4, 2, 17, 33, 45, 257007)),
            preserve_default=True,
        ),
    ]
