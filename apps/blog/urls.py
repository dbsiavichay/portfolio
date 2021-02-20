"""Blog URLs."""

# Django
from django.urls import path

# Views
from apps.blog.views import PostListView, PostDetailView

urlpatterns = [
    path(
        route='',
        view=PostListView.as_view(),
        name='home'
    ),
    path(
        route='post/<int:pk>/',
        view=PostDetailView.as_view(),
        name='post_detail'
    ),
]
