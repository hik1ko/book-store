import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

app = Celery('freelance_platform')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.timezone = "Asia/Tashkent"

app.autodiscover_tasks()
