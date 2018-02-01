from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from myapp.models import Article
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import datetime
from myapp.forms import RegisterForm
# Create your views here.

def fun_paginator(paginator,page):
    try:
        blogs=paginator.page(page)
    except PageNotAnInteger:
        blogs=paginator.page(1)
    except EmptyPage:
        blogs=paginator.page(paginator.num_pages)
    return blogs


def test(request):
    blogs=Article.objects.all()
    paginator=Paginator(blogs,2)
    page=request.GET.get('page')
    blogs=fun_paginator(paginator,page)

    return render_to_response("home.html",{'blogs':blogs})

def detail(request,b_id):
    try:
        blog = Article.objects.get(pk=str(b_id))
    except Exception as e:
        return HttpResponse(e)
    return render_to_response("detail.html", {'blog': blog})

def search_tag(request,b_tag):
    try:
        blogs = Article.objects.filter(category=b_tag)
        paginator = Paginator(blogs, 2)
        page = request.GET.get('page')
        blogs = fun_paginator(paginator, page)

    except Exception as e:
        return HttpResponse(e)
    return render_to_response("home.html", {'blogs': blogs})

def search_time(request,b_time):

    try:
        blogs = Article.objects.filter(date_time__contains=datetime.date(int(b_time[:4]),int(b_time[4:6]),int(b_time[6:8])))
        paginator = Paginator(blogs, 2)
        page = request.GET.get('page')
        blogs = fun_paginator(paginator, page)

    except Exception as e:
        return HttpResponse(e)
    return render_to_response("home.html", {'blogs': blogs})


def search_blog(request):
    error=[]
    global s
    if 'input_1' in request.GET:
        s=request.GET['input_1']
        if not s:
            error.append('请在搜索栏重新输入')
            return render_to_response("home.html",{'error':error})
        else:
            blogs=Article.objects.filter(title__icontains=s)
            paginator = Paginator(blogs, 2)
            page = request.GET.get('page')
            blogs = fun_paginator(paginator, page)
            if len(blogs)==0:
                error.append('未搜寻到相关记录')
                return render_to_response("home.html",{'blogs':blogs,'error':error})
            else:
                return render_to_response("home.html",{'blogs':blogs})
    blogs = Article.objects.filter(title__icontains=s)
    paginator = Paginator(blogs, 2)
    page = request.GET.get('page')
    blogs = fun_paginator(paginator, page)
    return render_to_response("home.html", {'blogs': blogs})

def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form=RegisterForm()
    return render(request,"register.html",{'form':form})


def index(request):
    return render(request,'index.html')