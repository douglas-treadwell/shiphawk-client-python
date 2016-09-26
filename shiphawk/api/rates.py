from .paths import rates_path


class RatesApi(object):
    def __init__(self, api):
        self.api = api

    def request(self, details):
        return self.api.post(rates_path(), json=details)['rates']
