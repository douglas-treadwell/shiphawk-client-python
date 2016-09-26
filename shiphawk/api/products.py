from .paths import products_path


class ProductsApi(object):
    def __init__(self, api):
        self.api = api

    def get(self, product_sku=None):
        return self.api.get(products_path(product_sku))

    def create(self, options):
        return self.api.post(products_path(), data=options)

    def delete(self, product_sku_or_skus):
        # NOTE: self.api.delete(products_path(a_product_sku)) does not work

        if isinstance(product_sku_or_skus, list):
            skus = product_sku_or_skus
        else:
            skus = [product_sku_or_skus]

        return self.api.delete(products_path(), json={'sku': skus})
