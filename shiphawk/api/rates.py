from .paths import rates_path


class RatesApi(object):
    def __init__(self, api):
        self.api = api

    def request(self, **details):
        """origin_address, destination_address, origin_accessorials=None, destination_accessorials=None"""

        return self.api.post(rates_path(), json=details)
