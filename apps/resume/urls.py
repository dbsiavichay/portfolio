"""Posts URLs."""

# Django
from django.urls import path

# Views
from apps.resume.views import TimelineListView

urlpatterns = [
    path(
        route='',
        view=TimelineListView.as_view(),
        name='home'
    ),
]
