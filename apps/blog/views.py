# Django
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

# Models
from apps.blog.models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
