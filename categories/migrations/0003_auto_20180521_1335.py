# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-21 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20180520_2241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='\u0418\u043c\u044f'),
        ),
    ]