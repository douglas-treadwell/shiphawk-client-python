from shiphawk import Client

import unittest

import os


def get_test_client(sandbox=True):
    if sandbox:
        return Client(api_token=os.environ['SHIPHAWK_SANDBOX_API_TOKEN'], sandbox=True)
    else:
        return Client(api_token=os.environ['SHIPHAWK_API_TOKEN'], sandbox=False)


class BaseTestCase(unittest.TestCase):
    def assertSuccessful(self, response):
        self.assertEquals(response.status_code // 100, 2)  # verify 2xx status
