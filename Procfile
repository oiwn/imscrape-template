api: gunicorn api:api -b 0.0.0.0:8888 -w 2 -k gevent
celery: celery -A job worker -B --loglevel=info
