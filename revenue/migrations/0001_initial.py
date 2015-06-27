# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemStoreMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemStoreSellDateMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sell_amount', models.FloatField()),
                ('sell_date', models.DateField(default=django.utils.timezone.now)),
                ('ItemStoreMap_id', models.ForeignKey(to='revenue.ItemStoreMap')),
            ],
        ),
        migrations.CreateModel(
            name='MenuGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_id', models.PositiveIntegerField()),
                ('group_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.PositiveIntegerField()),
                ('item_name', models.CharField(max_length=100)),
                ('group_id', models.ForeignKey(to='revenue.MenuGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_id', models.PositiveIntegerField()),
                ('store_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='itemstoremap',
            name='item_id',
            field=models.ForeignKey(to='revenue.MenuItem'),
        ),
        migrations.AddField(
            model_name='itemstoremap',
            name='store_id',
            field=models.ForeignKey(to='revenue.Store'),
        ),
    ]
