#coding:utf8
from __future__ import unicode_literals

from smtplib import SMTPRecipientsRefused

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.core.mail import send_mail


from test_proj.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, HOST


class Blog(models.Model):
    title_blog=models.CharField(max_length=255)
    def __unicode__(self):
        return '%s'%self.title_blog

class BlogPost(models.Model):
    id=models.AutoField(primary_key=True)
    blog=models.ForeignKey(Blog)
    title_post=models.CharField(
        max_length=255, default=u'Заголовок')
    text=models.TextField(default=u'Текст статьи')
    date_create=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '%s'%self.title_post

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print 'id=%s'%self.id

        super(BlogPost,self).save()
        for i in BlogUser.objects.get(blog__title_blog=self.blog).subscribers.all():
            print 'email=%s'%i.user.email
            try:
                send_mail('New Post',
                          'new post '+HOST+'/post'+str(self.id),
                          EMAIL_HOST_USER,
                          [i.user.email])
            except SMTPRecipientsRefused:
                print "message don't send 'SMTPRecipientsRefused'"
        print 'SUCCESS SEND'


class BlogUser(models.Model):
    id_user=models.AutoField(primary_key=True)
    user=models.OneToOneField(
        User,
        verbose_name=u'Пользователь')
    subscriptions=models.ManyToManyField(
        Blog,
        related_name='blog_list',
        null=True,
        blank=True,
        verbose_name=u'Подписки')
    read_p=models.ManyToManyField(
        BlogPost,
        related_name='post_list',
        null=True,
        blank=True,
        verbose_name=u'Прочтенные посты')
    blog=models.OneToOneField(
        Blog,
        verbose_name=u'Блог')
    subscribers=models.ManyToManyField(
        'self',
        null=True,
        blank=True,
        verbose_name=u'Подписчики')
    def __unicode__(self):
        return '%s'%self.user.username





