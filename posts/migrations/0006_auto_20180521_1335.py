# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-21 13:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_is_archive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Comment')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('name', 'author'), 'verbose_name': '\u041f\u043e\u0441\u0442', 'verbose_name_plural': '\u041f\u043e\u0441\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='posts', to='categories.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='posts.Post'),
        ),
    ]
