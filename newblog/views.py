from django.shortcuts import render,HttpResponse
from newblog.models import Post

# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'newblog/index.html', context={'post_list': post_list})