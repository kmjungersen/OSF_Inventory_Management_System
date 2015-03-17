# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('item_number', models.BigIntegerField()),
                ('expiration_date', models.DateTimeField()),
                ('cost', models.DecimalField(decimal_places='2', max_digits=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('barcode_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=200)),
                ('product_number', models.BigIntegerField()),
                ('date_first_added', models.DateTimeField(verbose_name='date added')),
                ('quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(to='inventory.Product'),
            preserve_default=True,
        ),
    ]
