# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-23 17:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='blog',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='test_app.Blog', verbose_name='\u0411\u043b\u043e\u0433'),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='read_p',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_list', to='test_app.BlogPost', verbose_name='\u041f\u0440\u043e\u0447\u0442\u0435\u043d\u043d\u044b\u0435 \u043f\u043e\u0441\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, null=True, related_name='blog_list', to='test_app.Blog', verbose_name='\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0438'),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]
