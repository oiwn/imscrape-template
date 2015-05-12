import logging
import argparse
from datetime import datetime

from weblib.logs import default_logging

from settings import db_connection, LOG_LEVEL, TASKS
from utils.scrapers_factory import ScrapersFactory


logger = logging.getLogger(__name__)


def setup_loggin():
    # setup default logging
    default_logging(grab_log='var/grab.log', level=LOG_LEVEL, mode='a',
                    propagate_network_logger=False,
                    network_log='var/grab.network.log')


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
        # remove dot due to
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


if __name__ == '__main__':
    setup_loggin()
    parser = argparse.ArgumentParser(description='command line interface')

    parser.add_argument("-T", "--task", type=str,
                        help="task to run")

    args = parser.parse_args()

    if args.task:
        scraper = ScrapersRunInterface.crawl(args.task)
        print(scraper.render_stats())
    else:
        parser.print_help()
