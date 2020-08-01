import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
app = Celery("core")  # core is just a name, it could be anything
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
