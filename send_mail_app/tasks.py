from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery_with_django import settings
from django.utils import timezone
from datetime import timedelta

from celery import shared_task

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    # timezone.localtime(users.date_time)
    for user in users:
        mail_subject = 'Hi!! Celery Testing'
        message = 'This is a test from celery'
        to_email = [user.email]
        print("to_emailto_email",to_email)
        send_mail(
            subject = mail_subject,
            message = message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = to_email,
            fail_silently = False,
            )
    return "Done"