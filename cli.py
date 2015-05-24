import logging
import argparse

from weblib.logs import default_logging

from tasks import run_task
from settings import LOG_LEVEL
from utils.run_interface import ScrapersRunInterface


logger = logging.getLogger(__name__)


def setup_loggin():
    # setup default logging
    default_logging(grab_log='var/grab.log', level=LOG_LEVEL, mode='a',
                    propagate_network_logger=False,
                    network_log='var/grab.network.log')


if __name__ == '__main__':
    setup_loggin()
    parser = argparse.ArgumentParser(description='command line interface')

    parser.add_argument("-T", "--task", type=str,
                        help="task to run")
    parser.add_argument('-c', '--celery', action="store_true", default=False,
                        help='run as celery task')

    args = parser.parse_args()

    if args.task:
        # scraper = ScrapersRunInterface.crawl(args.task)
        # print(scraper.render_stats())
        if args.celery:
            scraper_results = run_task.delay(args.task)
            logger.info(scraper_results)
        else:
            scraper = ScrapersRunInterface.crawl(args.task)
            logger.info(scraper.render_stats())
    else:
        parser.print_help()
