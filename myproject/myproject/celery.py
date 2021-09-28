from __future__ import absolute_import
from __future__ import unicode_literals

import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# здесь вы меняете имя app
app = Celery('myproject')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'create_new_object': {
        'task': 'apptask.tasks.create_new_object',
        'schedule': 13.0,
    }
}