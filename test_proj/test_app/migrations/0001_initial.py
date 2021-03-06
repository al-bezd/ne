# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-20 16:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_blog', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_post', models.CharField(default='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', max_length=255)),
                ('text', models.TextField(default='\u0422\u0435\u043a\u0441\u0442 \u0441\u0442\u0430\u0442\u044c\u0438')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Blog')),
                ('read_p', models.ManyToManyField(blank=True, null=True, to='test_app.BlogPost')),
                ('subscriptions', models.ManyToManyField(blank=True, null=True, related_name='blog_id', to='test_app.Blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
