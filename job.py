from celery import Celery

from settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND, CELERY_CONFIG


celery_app = Celery('tasks', backend=CELERY_RESULT_BACKEND, broker=CELERY_BROKER_URL)
celery_app.conf.update(CELERY_CONFIG)
