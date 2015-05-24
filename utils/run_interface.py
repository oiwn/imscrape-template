from datetime import datetime

from settings import db_connection, TASKS
from utils.scrapers_factory import ScrapersFactory


class ScrapersRunInterface(object):
    tasks = TASKS
    db = db_connection()

    @classmethod
    def crawl(cls, task_name):
        scraper_module = cls.tasks[task_name]
        scraper_instance = ScrapersFactory.run_instance(scraper_module)
        cls.saveStats(task_name, scraper_instance)
        return scraper_instance

    @classmethod
    def saveStats(cls, task_name, scraper_instance):
        # remove dots due to
        # bson.errors.InvalidDocument: key 'response_handler.task_repo' must not contain '.'
        timers = {k.replace('.', '_'): v for k, v in scraper_instance.stat.timers.items()}
        stats = {
            'task_name': task_name,
            'crawler': cls.tasks[task_name],
            'counters': scraper_instance.stat.counters,
            'timers': timers,
            '_created': datetime.utcnow(),
        }
        cls.db['scrapersStats'].insert(stats)
        return stats
