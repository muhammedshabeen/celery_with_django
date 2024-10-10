from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django.contrib.auth import get_user_model

# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_mail_func.delay()
    users = get_user_model().objects.all()
    for user in users:
        print("user email",user.email)
    return HttpResponse("Mail Sent Successfully")

    