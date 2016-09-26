from . import get_test_client, BaseTestCase

from shiphawk.errors import NotFoundError

import uuid


class ProductsApiTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = get_test_client()

        # for tests that use a single sku
        cls.sku = cls.get_sku()

        # for tests that use many skus
        cls.skus = [cls.get_sku() for _ in range(0, 3)]

    @staticmethod
    def get_sku():
        return str(uuid.uuid4())

    def test_1_create_product(self):
        self.client.products.create({'sku': self.sku})

    def test_2_get_product(self):
        self.client.products.get(self.sku)

    def test_3_delete_product(self):
        self.client.products.delete(self.sku)

        with self.assertRaises(NotFoundError):
            self.client.products.get(self.sku)

    def test_4_get_all_products(self):
        skus = self.skus

        previous_sku_count = len(self.client.products.get())

        for sku in skus:
            self.client.products.create({'sku': sku})

        new_sku_count = len(self.client.products.get())

        self.assertEqual(new_sku_count, previous_sku_count + len(skus))

    def test_5_delete_multiple_products(self):
        self.client.products.delete(self.skus)
