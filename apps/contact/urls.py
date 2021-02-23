# Django
from django.urls import path

# Views
from .views import ContactView

urlpatterns = [
    path(
        route="message/send/",
        view=ContactView.as_view(),
        name="send_message",
    ),
]