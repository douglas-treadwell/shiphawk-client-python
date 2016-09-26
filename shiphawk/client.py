import requests

from .api import Api


class Client(object):
    VERSION = '0.0.1'

    PRODUCTION_API_HOST = 'https://shiphawk.com'
    SANDBOX_API_HOST = 'https://sandbox.shiphawk.com'
    DEFAULT_API_VERSION = 'v4'

    def __init__(self, **options):
        from .shiphawk import Shiphawk

        if options.pop('sandbox', False) or Shiphawk.sandbox:
            host = Client.SANDBOX_API_HOST
        else:
            host = Client.PRODUCTION_API_HOST

        self.options = options

        self.api_token = options.pop('api_token', Shiphawk.api_token)
        self.api_version = options.pop('api_version', Client.DEFAULT_API_VERSION)
        self.host_url = options.pop('host_url', host)
        self.requests = options.pop('requests', requests)

        self.api = Api(self)

        self.products = self.api.products

    def __getattr__(self, attr):
        return getattr(self.api, attr)
