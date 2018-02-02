from django.conf.urls import url

from newblog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]