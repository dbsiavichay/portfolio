# Django
from django.urls import reverse_lazy
from django.views.generic import View, ListView
from django.http import HttpResponse
from django.conf import settings

# Models
from apps.resume.models import Timeline, Skill, Knowledge, Language


class TimelineListView(ListView):
    model = Timeline

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'skills': Skill.objects.all(),
            'knowledges': Knowledge.objects.all(),
            'languages': Language.objects.all()
        })
        return context


class DownloadResumeView(View):
    def get(self, request, *args, **kwargs):

        with open(settings.BASE_DIR + '/static/pdf/denis_resume.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

        pdf.close()
        return response
