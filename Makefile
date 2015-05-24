.PHONY: runapp runapi clean

runapi:
	python api.py

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete

clean-task-queue:
	celery purge --app=job.celery_app
