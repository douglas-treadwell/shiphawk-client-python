from . import get_test_client, BaseTestCase, pallets


class RatesApiTest(BaseTestCase):
    minimal_origin_address = {'zip': '94107'}
    minimal_destination_address = {'zip': '02108'}

    @classmethod
    def setUpClass(cls):
        cls.client = get_test_client()

    def test_request_rate(self):
        self.client.rates.request({
            'origin_address': self.minimal_origin_address,
            'destination_address': self.minimal_destination_address,
            'items': pallets(4)
        })
