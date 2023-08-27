from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"

class PostDetail(generic.DetailView):
     model = Post
     template_name = "post_detail.html"

class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

class UserProfile(generic.DetailView):
    model = Post
    template_name = "user_profile.html"

