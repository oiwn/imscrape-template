from settings import SCRAPER_CONFIG, DB_URI, DB_NAME

from .moduleimport import module_import


class ScrapersFactory(object):
    """
    Configure grab spider instance
    """

    @classmethod
    def get_instance(cls, spider_class, use_proxy=False, use_cache=True, **kwargs):
        """ Configure bot instance.
        """

        if isinstance(spider_class, basestring):
            spider_cls = module_import(spider_class)
        else:
            spider_cls = spider_class

        bot = spider_cls(**SCRAPER_CONFIG)

        if use_proxy:
            # need proxy list
            bot.load_proxylist('var/proxylist.txt', 'text_file', 'http', auto_change=True)
        if use_cache:
            host = DB_URI.format('')  # leave database param empty

            bot.setup_cache(
                backend='mongo',
                database=DB_NAME,
                use_compression=True, host=host)

        bot.setup_grab(timeout=20, connect_timeout=20)

        for key, value in kwargs.items():
            setattr(bot, key, value)

        return bot

    @classmethod
    def run_instance(cls, spider_class, use_proxy=False, use_cache=True, **kwargs):
        """ Configure and run bot instance
        """
        scraper_instance = cls.get_instance(
            spider_class, use_proxy=use_proxy, use_cache=use_cache, **kwargs)
        scraper_instance.run()
        return scraper_instance
