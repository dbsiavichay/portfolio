# Django
from django.urls import reverse_lazy
from django.views.generic import ListView

# Models
from apps.portfolio.models import Category, Project


class ProjectListView(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.all(),
        })
        return context
