import os
from celery import Celery





os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FetchApi.settings")
app = Celery("FetchApi")
app.config_from_object("django.conf:settings", namespace="CELERY")

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()



