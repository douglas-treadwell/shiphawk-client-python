from .client import Client


class Shiphawk(object):
    sandbox = False
    api_token = None

    def __getattr__(self, attr):
        return getattr(Client(), attr)
