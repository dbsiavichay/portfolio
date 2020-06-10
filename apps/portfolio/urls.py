"""Portfolio URLs."""

# Django
from django.urls import path

# Views
from apps.portfolio.views import ProjectListView

urlpatterns = [
    path(
        route='',
        view=ProjectListView.as_view(),
        name='home'
    ),
]
