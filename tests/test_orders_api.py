from . import get_test_client, BaseTestCase

import time


class OrdersApiTest(BaseTestCase):
    # for tests that use a single order
    order_number = int(time.time())
    updated_order_number = order_number + 1

    # for tests that use many orders
    order_numbers = [order_number + 2, order_number + 3, order_number + 4]

    # to communicate between sequential tests
    order_id = None
    order = None

    @classmethod
    def setUpClass(cls):
        cls.client = get_test_client()

    def test_1_create_order(self):
        response = self.client.orders.create({'order_number': self.order_number})
        OrdersApiTest.order_id = response['id']
        OrdersApiTest.order = response

    def test_2_get_order(self):
        response = self.client.orders.get(OrdersApiTest.order_id)
        self.assertEqual(response['order_number'], str(self.order_number))

    def test_3_update_order(self):
        self.client.orders.update({
            'id': OrdersApiTest.order_id,
            'order_number': self.updated_order_number
        })
        response = self.client.orders.get(OrdersApiTest.order_id)
        self.assertEqual(response['order_number'], str(self.updated_order_number))

    def test_4_cancel_order(self):
        self.client.orders.cancel(OrdersApiTest.order_id)
        response = self.client.orders.get(OrdersApiTest.order_id)
        self.assertEqual(response['status'], 'cancelled')

    '''
    Note that the sandbox appears to be limited to 100 orders, after which
    we can continue to create orders but the number of orders doesn't change.
    I assume older orders are being deleted as new orders are added.
    '''
    def test_5_get_all_orders(self):
        order_numbers = self.order_numbers

        previous_order_count = len(self.client.orders.get())

        if previous_order_count > 1:
            return

        for order_number in OrdersApiTest.order_numbers:
            self.client.orders.create({'order_number': order_number})

        new_order_count = len(self.client.orders.get())

        self.assertEqual(new_order_count, previous_order_count + len(order_numbers))
