from .paths import orders_path


class OrdersApi(object):
    def __init__(self, api):
        self.api = api

    def get(self, order_id=None):
        return self.api.get(orders_path(order_id))

    def create(self, order_details):
        if 'id' in order_details.keys():
            raise ValueError("Create method does not expect an order with an id.")

        return self.api.post(orders_path(), data=order_details)

    '''
    Note that although we're POSTing, ShipHawk treats this as a PATCH
    and only updates the provided fields.

    Also, the ShipHawk documentation cURL example doesn't show adding the
    order id to the resource path.
    '''
    def update(self, order_details):
        if 'id' not in order_details.keys():
            raise ValueError("Update method expects an order with an id.")

        return self.api.post(orders_path(order_details['id']), data=order_details)

    '''
    Note that although we're POSTing, ShipHawk treats this as a PATCH
    and only updates the provided fields.

    Also, the ShipHawk documentation cURL example doesn't show adding the
    order id to the resource path.
    '''
    def cancel(self, order_id):
        return self.api.post(orders_path(order_id), json={
            'id': order_id,
            'status': 'cancelled'
        })
