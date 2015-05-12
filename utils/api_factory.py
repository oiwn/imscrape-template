from eve import Eve


from settings import EVE_CONFIG, DEBUG


class ApiFactory(object):
    """ Configure python eve API instance
    """

    @classmethod
    def get_instance(cls, settings=EVE_CONFIG, debug=DEBUG):
        """ Configure and run bot instance.

        """

        app = Eve(settings=settings)
        app.debug = debug
        return app
