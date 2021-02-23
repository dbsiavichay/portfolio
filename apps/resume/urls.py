"""Resume URLs."""

# Django
from django.urls import path

# Views
from apps.resume.views import TimelineListView, DownloadResumeView

urlpatterns = [
    path(
        route='',
        view=TimelineListView.as_view(),
        name='home'
    ),
    path(
        route='download/',
        view=DownloadResumeView.as_view(),
        name='download_resume'
    ),
]
