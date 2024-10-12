from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django.contrib.auth import get_user_model
from django_celery_beat.models import PeriodicTask, CrontabSchedule 
import json

# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Mail Sent Successfully")


# Create dunamic celery

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=1,minute=13)
    task = PeriodicTask.objects.create(crontab=schedule, name='schedule_mail_task_'+'3',task='send_mail_app.tasks.send_mail_func') 
    # args=json.dumps((1,2)))
    return HttpResponse("Done") 




    