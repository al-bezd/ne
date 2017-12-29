#coding:utf8
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.decorators import user_passes_test
from test_app.views import to_follow, del_follow, add_read, create_post
from test_app.views import blog, free_blogs, my_subscrip, news, post_page




urlpatterns = [
    url(r'^my_subscrip', user_passes_test(lambda u: u.is_active,login_url='/auth')(my_subscrip), name='my_subscrip'),
    url(r'^free_blogs', user_passes_test(lambda u: u.is_active,login_url='/auth')(free_blogs), name='free_blogs'),
    url(r'auth',login,{'template_name':'test_app/auth.html',
                       'redirect_field_name':'blog'}),
    url(r'^blog', user_passes_test(lambda u: u.is_active)(blog), name='blog'),
    url(r'^news', user_passes_test(lambda u: u.is_active)(news), name='news'),
    url(r'^to_follow',to_follow),
    url(r'^del_follow', del_follow),
    url(r'^add_read', add_read),
    url(r'post(?P<id>[^/]+)', post_page),
    url(r'create_post',create_post),
    url(r'^', user_passes_test(lambda u: u.is_active,login_url='/auth')(blog), name='blog'),
]
