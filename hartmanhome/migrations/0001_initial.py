# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flat_data',
            fields=[
                ('i_d', models.IntegerField(primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('free_text', models.CharField(max_length=30)),
            ],
        ),
    ]