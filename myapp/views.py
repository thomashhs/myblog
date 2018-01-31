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
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、确认密码、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
    return render(request, 'register.html', context={'form': form, 'next': redirect_to})


def index(request):
    return render(request,'index.html')