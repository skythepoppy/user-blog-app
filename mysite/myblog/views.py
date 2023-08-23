from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    query = Post.objects.filter(status=1).order_by("-created_on")
    template = "index.html"

class PostDetail(generic.DetailView):
     model = Post
     template = "post_detail.html"