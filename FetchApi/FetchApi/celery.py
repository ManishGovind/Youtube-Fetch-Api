from asyncio import tasks
import os
from celery import Celery
from celery.schedules import crontab





os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FetchApi.settings")
app = Celery('FetchApi')
app.config_from_object("django.conf:settings", namespace="CELERY")

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()



    



app.conf.beat_schedule = {
    
    'fetchs videos every 30 seconds': {
        "task": "api.tasks.save_videos",
        "schedule": crontab(minute="*/1"),
    },
}

app.conf.timezone = 'Asia/Kolkata'



