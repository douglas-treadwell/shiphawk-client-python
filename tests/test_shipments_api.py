from . import get_test_client, BaseTestCase, pallets, ignore_payment_errors

import unittest


class ShipmentsApiTest(BaseTestCase):
    minimal_origin_address = {'zip': '94107'}
    minimal_destination_address = {'zip': '02108'}

    origin_address = {
        'street1': '345 Ritch St',
        'city': 'San Francisco',
        'state': 'CA',
        'zip': '94107'
    }

    destination_address = {
        'street1': '1400 Centre Circle',
        'city': 'Downers Grove',
        'state': 'IL',
        'zip': '60515'
    }

    @classmethod
    def setUpClass(cls):
        cls.client = get_test_client()

    def get_zipcode_rates(self):
        return self.client.rates.request({
            'origin_address': self.origin_address,
            'destination_address': self.destination_address,
            'items': pallets(4)
        })

    def get_rates(self):
        return self.client.rates.request({
            'origin_address': self.origin_address,
            'destination_address': self.destination_address,
            'items': pallets(4)
        })

    @unittest.expectedFailure  # address details are required to create a shipment
    def test_create_shipment_from_zipcode_rate(self):
        rates = self.get_zipcode_rates()

        accepted_rate = rates[0]

        self.client.shipments.create(rate_id=accepted_rate['id'],
                                     origin_address=self.minimal_origin_address,
                                     destination_address=self.minimal_destination_address)

    '''
    Note: Will fail if Stripe hasn't been configured for the ShipHawk account.

    "Your account does not have a stripe_customer_id and is unable to book
     shipments using ShipHawk's tariffs"
    '''
    @unittest.skipIf(ignore_payment_errors, "will fail even in sandbox if payment method isn't configured")
    def test_create_shipment_from_rate(self):
        rates = self.get_rates()

        accepted_rate = rates[0]

        self.client.shipments.create(rate_id=accepted_rate['id'],
                                     origin_address=self.origin_address,
                                     destination_address=self.destination_address)
