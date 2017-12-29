#coding:utf8
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

from models import Blog, BlogPost, BlogUser

context={}
def blog(request):
    context['blog'] = BlogUser.objects.get(user=User.objects.get(username=request.user.username))
    context['post'] = BlogPost.objects.filter(blog=context['blog'].blog)
    context.update(csrf(request))
    response = render(request, 'test_app/blog.html', context)
    return response

def news(request):
    b=BlogUser.objects.get(user=request.user)
    a=b.subscriptions.all().exclude(title_blog=b.blog)

    context['post'] = BlogPost.objects.filter(blog__in=b.subscriptions.exclude(title_blog=b.blog)).order_by('-date_create')
    print context['post']
    context['post_read'] = b.read_p.all()
    context.update(csrf(request))
    response = render(request, 'test_app/news.html', context)
    return response

def my_subscrip(request):
    user=User.objects.get(username=request.user.username)
    b=BlogUser.objects.get(user=user)

    context['my_subscrip'] = b.subscriptions.exclude(title_blog=b.blog)
    print b.subscriptions.all().exclude(title_blog=b.blog).values_list('id')
    context.update(csrf(request))
    response = render(request, 'test_app/my_subscrip.html', context)
    return response

def free_blogs(request):
    #__dict__ prosmotr vseh atributov objecta
    user=User.objects.get(username=request.user.username)
    b=BlogUser.objects.get(user=user)

    context['free_blog']=Blog.objects.exclude(title_blog__in=b.subscriptions.all().values_list('title_blog')).exclude(title_blog=b.blog.title_blog)

    context.update(csrf(request))
    response = render(request, 'test_app/free_blog.html', context)
    return response

def post_page(request, id):
    user = User.objects.get(username=request.user.username)
    post=BlogPost.objects.get(id=id)

    context['post'] = post

    context.update(csrf(request))
    response = render(request, 'test_app/post_page.html', context)
    return response



@csrf_protect
def to_follow(request):
    if request.POST.get('id'):
        u=BlogUser.objects.get(user=User.objects.get(username=request.user.username))
        u.subscriptions.add(Blog.objects.get(id=request.POST.get('id')))


        user = User.objects.get(username=request.user.username)
        BlogUser.objects.get(blog__id=request.POST.get('id')).subscribers.add(BlogUser.objects.get(user=user))

        response = render(request, 'test_app/free_blog.html', context)
        return response

@csrf_protect
def del_follow(request):
    if request.POST.get('id'):
        blog=Blog.objects.get(id=request.POST.get('id'))
        u=BlogUser.objects.get(user=User.objects.get(username=request.user.username))
        u.subscriptions.remove(blog)

        print 'blog %s'%BlogPost.objects.filter(blog__id=request.POST.get('id')).values_list('id')
        for i in BlogPost.objects.filter(blog__id=request.POST.get('id')):
            print i
            u.read_p.remove(i)


        user = User.objects.get(username=request.user.username)
        BlogUser.objects.get(blog__id=request.POST.get('id')).subscribers.remove(BlogUser.objects.get(user=user))

        response = render(request, 'test_app/my_subscrip.html', context)
        return response

@csrf_protect
def add_read(request):
    if request.POST.get('id'):
        u=BlogUser.objects.get(user=User.objects.get(username=request.user.username))
        u.read_p.add(BlogPost.objects.get(id=request.POST.get('id')))
        u.save
        return HttpResponse('nice')

@csrf_protect
def create_post(request):
    if request.POST.get('title_post'):
        post=BlogPost(
            blog=BlogUser.objects.get(user=request.user).blog,
            title_post=request.POST['title_post'],
            text=request.POST['body_post'])
        post.save()
    context['blog'] = BlogUser.objects.get(user=User.objects.get(username=request.user.username))
    response = render(request, 'test_app/create_post.html', context)
    return response

