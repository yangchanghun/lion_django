

from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = "posts"
    paginate_by = 1

# # views.py
# from django.shortcuts import render
# from .models import Post
# from django.views.generic import ListView
# # Create your views here.

# class PostListView(ListView):
#     model = Post
#     template_name = "blog/post_all.html"
#     context_object_name = 'posts'
#     paginate_by = 1