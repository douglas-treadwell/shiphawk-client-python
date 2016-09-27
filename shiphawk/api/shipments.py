from .paths import shipments_path


class ShipmentsApi(object):
    def __init__(self, api):
        self.api = api

    def get(self, shipment_id=None):
        return self.api.get(shipments_path(shipment_id))

    '''
    Note: There is also a way to manually create a shipment without a rate_id
    by providing many other required details, but ShipHawk warns about doing this
    on their website, so the client only provides the recommended method.
    '''
    def create(self, rate_id, origin_address, destination_address):
        return self.api.post(
            shipments_path(),
            json={
                'rate_id': rate_id,
                'origin_address': origin_address,
                'destination_address': destination_address
            })

    def add_external(self, shipment_details):
        return self.api.post(shipments_path(), json=shipment_details)

    def update(self, shipment_details):
        if 'id' not in shipment_details.keys():
            raise ValueError("Update method expects a shipment with an id.")

        return self.api.post(shipments_path(shipment_details['id']), json=shipment_details)

    def cancel(self, shipment_id):
        return self.api.delete(shipments_path(shipment_id))
