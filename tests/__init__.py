from shiphawk import Client

import unittest

import os


ignore_payment_errors = os.environ.get('SHIPHAWK_IGNORE_PAYMENT_ERRORS', None) == 'true'


def get_test_client():
    return Client(api_token=os.environ.get('SHIPHAWK_SANDBOX_API_TOKEN', None), sandbox=True)


class BaseTestCase(unittest.TestCase):
    def assertSuccessful(self, response):
        self.assertEquals(response.status_code // 100, 2)  # verify 2xx status


def pallet():
    return {
        'type': 'handling_unit',
        'handling_unit_type': 'pallet',
        'length': 48,
        'width': 40,
        'height': 60,
        'value': 1000,
        'freight_class': 200,
        'package_type': 'box',
        'package_quantity': 125
    }


def pallets(quantity):
    return [pallet() for _ in range(0, quantity)]
