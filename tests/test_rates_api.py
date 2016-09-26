from . import get_test_client, BaseTestCase, pallets


class RatesApiTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = get_test_client()

        cls.origin_address = {'zip': '94107'}
        cls.destination_address = {'zip': '02108'}

    def test_request_rate(self):
        response = self.client.rates.request({
            'origin_address': self.origin_address,
            'destination_address': self.destination_address,
            'items': pallets(4)
        })

        self.assertTrue('rates' in response.keys())
