from django.shortcuts import render, get_object_or_404

from .models import Post
from django.http import Http404


# Create your views here.

def post_list(request):
    posts = Post.published.all()
    return render(request,'blog/blog/post/list.html',{'posts':posts})

from django.http import Http404

def post_detail(request, id):
    post= get_object_or_404(Post, id=id,status=Post.Status.PUBLISHED)
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404 ("No post found.")
    return render(request,'blog/blog/post/detail.html', {'post':post})

