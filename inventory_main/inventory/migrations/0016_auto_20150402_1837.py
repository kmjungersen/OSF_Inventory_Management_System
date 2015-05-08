# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_auto_20150402_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('room_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocationShelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('shelf_id', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocationUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('unit_id', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('temperature', models.CharField(max_length=200, null=True)),
                ('room', models.ForeignKey(to='inventory.LocationRoom')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Supplier',
            new_name='Distributor',
        ),
        migrations.AddField(
            model_name='locationshelf',
            name='unit',
            field=models.ForeignKey(to='inventory.LocationUnit'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='distributor',
            old_name='supplier_name',
            new_name='distributor_name',
        ),
        migrations.AddField(
            model_name='item',
            name='distributor',
            field=models.ForeignKey(to='inventory.Distributor', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2016, 4, 1, 18, 37, 36, 647735)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='date_first_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 2, 18, 37, 36, 646876), verbose_name='date added'),
            preserve_default=True,
        ),
    ]
