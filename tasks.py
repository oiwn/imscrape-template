import sys

from job import celery_app
from utils.run_interface import ScrapersRunInterface
from settings import BASE_DIR


@celery_app.task
def run_task(task_name):
    # add current dir into system path
    # got import error without it
    sys.path.append(BASE_DIR)

    scraper = ScrapersRunInterface.crawl(task_name)
    return scraper.stat.counters
