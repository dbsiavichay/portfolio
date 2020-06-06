# Django
from django.urls import reverse_lazy
from django.views.generic import ListView

# Models
from apps.resume.models import Timeline, Skill, Language


class TimelineListView(ListView):
    model = Timeline

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'skills': Skill.objects.all(),
            'languages': Language.objects.all()
        })
        return context
