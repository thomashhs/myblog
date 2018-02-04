"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', views.test,name='test'),
    url(r'^(?P<b_id>\d+)/$', views.detail,name="detail"),
    url(r'^tag/(?P<b_tag>\w+)/$', views.search_tag,name="search_tag"),
    url(r'^time/(?P<b_time>\w+)/$', views.search_time,name="search_time"),
    url(r'^search/$', views.search_blog,name="search_blog"),
    url(r'^ueditor/',include("DjangoUeditor.urls")),

    url(r'^users/', include('myapp.urls')),
    url(r'^users/', include("django.contrib.auth.urls")),
    url(r'^$', views.index,name="index"),

    url(r'^newblog/', include('newblog.urls')),

    url(r'^comments/', include('comments.urls')),

]

