from .paths import orders_path


class OrdersApi(object):
    def __init__(self, api):
        self.api = api

    def get(self, order_id=None):
        return self.api.get(orders_path(order_id))

    def create_or_update(self, order_details):
        return self.api.post(orders_path(), data=order_details)

    def create(self, order_details):
        if 'id' in order_details.keys():
            raise ValueError("Create method does not expect an order with an id.")

        return self.create_or_update(order_details)

    def update(self, order_details):  # same action as create, but details includes id
        if 'id' not in order_details.keys():
            raise ValueError("Update method expects an order with an id.")

        return self.create_or_update(order_details)

    def cancel(self, order_id):
        return self.api.post(orders_path(), json={
            'id': order_id,
            'status': 'cancelled'
        })
