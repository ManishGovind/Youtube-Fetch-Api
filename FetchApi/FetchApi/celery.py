import os
from celery import Celery
from celery.schedules import crontab





os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FetchApi.settings")
app = Celery('FetchApi')
app.config_from_object("django.conf:settings", namespace="CELERY")

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()



app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'fetchs videos every 30 seconds': {
        'task': 'tasks.save_videos',
        'schedule': crontab(seconds=30),
        'args': (16, 16),
    },
}

app.conf.timezone = 'Asia/Kolkata'

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


