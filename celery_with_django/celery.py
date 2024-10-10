from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_with_django.settings')

app = Celery('celery_with_django')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# CELERY BEAT SETTINGS
app.conf.beat_schedule = {
    'send-email-every-day-at-8' : {
        'task' : 'send_mail_app.tasks.send_mail_func',
        'schedule' : crontab(hour=21, minute=16)
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

