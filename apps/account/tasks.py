import os

from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_email(subject, message, recipient_list):
    send_mail(subject, message, os.getenv('EMAIL_HOST_USER'), recipient_list)
