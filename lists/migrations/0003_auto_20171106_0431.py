# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 04:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20171102_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('list', 'text')]),
        ),
    ]
