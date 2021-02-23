from django.views.generic import FormView
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings


from .forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm

    def form_valid(self, form):
        message = form.cleaned_data['message']
        message = message + "\n\n FROM: " + form.cleaned_data['email']
        send_mail(
            form.cleaned_data['subject'], message,
            f"{form.cleaned_data['name']} (Mailjet)  <{settings.DEFAULT_FROM_EMAIL}>",
            [settings.DEFAULT_FROM_EMAIL],
        )

        return JsonResponse({
            'type': 'success',
            'message': 'Your message has been sent.',
        })

    def form_invalid(self, form):
        return JsonResponse({
            'type': 'danger',
            'message': 'Corriga los errores y vuelva a intentar.',
        })
