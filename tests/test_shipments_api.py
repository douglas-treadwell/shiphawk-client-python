from . import get_test_client, BaseTestCase, pallets
from shiphawk import UnprocessableEntityError

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

    # to communicate between sequential tests
    shipment_id = None

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

    def add_external_shipment(self):
        return self.client.shipments.add_external({
            'origin_address': self.origin_address,
            'destination_address': self.destination_address,
            'carrier_code': 'ups',  # not required
            'service_level': 'UPS Ground'  # not required
        })

    @unittest.expectedFailure  # address details are required to create a shipment
    def test_create_shipment_from_zipcode_rate(self):
        rates = self.get_zipcode_rates()

        accepted_rate = rates[0]

        self.client.shipments.create(rate_id=accepted_rate['id'],
                                     origin_address=self.minimal_origin_address,
                                     destination_address=self.minimal_destination_address)

    def test_add_external_shipment(self):
        self.add_external_shipment()

    def test_1_create_shipment_from_rate(self):
        rates = self.get_rates()

        accepted_rate = rates[0]

        # the except handler below is a workaround for ShipHawk sandbox
        # accounts not set up to allow creating shipments, which requires
        # a ShipHawk administrator to set up a stripe_customer_id

        try:
            shipment = self.client.shipments.create(
                rate_id=accepted_rate['id'],
                origin_address=self.origin_address,
                destination_address=self.destination_address)
        except UnprocessableEntityError as error:
            try:
                if 'stripe_customer_id' in error.response.json()['error']:
                    shipment = self.add_external_shipment()
                else:
                    raise error
            except:
                raise error

        ShipmentsApiTest.shipment_id = shipment['id']

    def test_2_get_shipment(self):
        self.client.shipments.get(ShipmentsApiTest.shipment_id)

    def test_3_update_shipment(self):
        # note that the status field is required in updates
        # although this is not mentioned in the API documentation

        self.client.shipments.update({
            'id': ShipmentsApiTest.shipment_id,
            'tracking_number': 101,
            'status': 'ordered'
        })

        shipment = self.client.shipments.get(ShipmentsApiTest.shipment_id)
        self.assertEqual(shipment['tracking_number'], str(101))

    def test_4_cancel_shipment(self):
        self.client.shipments.cancel(ShipmentsApiTest.shipment_id)

        shipment = self.client.shipments.get(ShipmentsApiTest.shipment_id)
        self.assertEqual(shipment['status'], 'cancelled')
