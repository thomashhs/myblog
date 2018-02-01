from django.conf.urls import url
from myapp import views

app_name = 'myapp'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
]