
from django.urls import path
from .views import *

urlpatterns = [
    path('',test,name="test"),
    path('send_mail',send_mail_to_all,name="send_mail_to_all"),
    path('schedule_mail',schedule_mail,name="schedule_mail"),
]
