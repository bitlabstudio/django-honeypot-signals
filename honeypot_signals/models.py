"""Signal handler if someone tries to login on an invalid admin url."""
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.dispatch import receiver
from django.template.loader import render_to_string

from admin_honeypot.signals import honeypot


@receiver(honeypot)
def send_notification(sender, instance, **kwargs):
    ctx_dict = {
        'object': instance,
        'site': Site.objects.get_current()
    }
    subject = render_to_string(
            'honeypot_signals/notification_subject.txt',
            ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    message = render_to_string('honeypot_signals/notification.txt', ctx_dict)
    to = [item[1] for item in settings.MANAGERS]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, to)
