from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render, get_object_or_404
import markdown

from blog_web.models import Post, Category


def index(request):
    # return HttpResponse("欢迎来到我的博客")
    # return render(request, 'blog_web/index.html', context={
    #     'title': '博客首页',
    #     'welcome': 'welcome to my personal page'
    #     })
    post_list = Post.objects.all()
    return render(request, "blog_web/index.html", context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request, 'blog_web/detail.html', context={'post': post})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    )
    return render(request, "blog_web/index.html", context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, "blog_web/index.html", context={'post_list': post_list})

