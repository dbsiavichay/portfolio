# Django
from django.urls import reverse_lazy
from django.views.generic import ListView

# Models
from apps.resume.models import Timeline


class TimelineListView(ListView):
    model = Timeline
