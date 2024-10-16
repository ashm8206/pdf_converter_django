from __future__ import absolute_import, unicode_literals
from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'img_to_pdf_app.settings')

app = Celery('img_to_pdf_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()