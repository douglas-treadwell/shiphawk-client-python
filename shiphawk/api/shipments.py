from .paths import shipments_path, shipment_labels_path, shipment_notes_path
from .paths import shipment_commercial_invoice_path, shipment_tracking_path
from .paths import shipment_bill_of_lading_path
from .paths import external_shipments_path


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
        return self.api.post(external_shipments_path(), json=shipment_details)

    def update(self, shipment_details):
        if 'id' not in shipment_details.keys():
            raise ValueError("Update method expects a shipment with an id.")

        return self.api.post(shipments_path(shipment_details['id']), json=shipment_details)

    def cancel(self, shipment_id):
        return self.api.delete(shipments_path(shipment_id))

    def get_commercial_invoice(self, shipment_id, refresh=False):
        # code duplication below is to avoid adding the regen_pdf
        # query string parameter unless needed

        if not refresh:
            return self.api.get(
                shipment_commercial_invoice_path(shipment_id),
            )
        else:
            return self.api.get(
                shipment_commercial_invoice_path(shipment_id),
                {'regen_pdf': True}
            )

    def get_bill_of_lading(self, shipment_id, refresh=False, carrier_code=None):
        if not refresh and not carrier_code:
            return self.api.get(
                shipment_bill_of_lading_path(shipment_id),
            )
        elif carrier_code:
            return self.api.get(
                shipment_bill_of_lading_path(shipment_id),
                {
                    'carrier_code': carrier_code
                }
            )
        elif refresh:  # carrier_code is required in this case
            return self.api.get(
                shipment_bill_of_lading_path(shipment_id),
                {
                    'regen_pdf': True,
                    'carrier_code': carrier_code
                }
            )

    def get_bol(self, *args, **kwargs):
        return self.get_bill_of_lading(*args, **kwargs)

    def track(self, shipment_id):
        return self.api.get(shipment_tracking_path(shipment_id))

    def set_tracking_callback(self, shipment_id, callback_url):
        return self.api.post(
            shipment_tracking_path(shipment_id),
            json={'callback_url': callback_url}
        )

    def create_label(self, shipment_id, label_format=None):
        if not label_format:  # defaults to PDF, but leave that to the server
            return self.api.post(
                shipment_labels_path(shipment_id)
            )
        else:
            return self.api.post(
                shipment_labels_path(shipment_id),
                {'label_format': label_format}
            )

    def get_labels(self, shipment_id):
        return self.api.get(shipment_labels_path(shipment_id))

    def create_note(self, shipment_id, body, tag=None):
        """
        :param shipment_id: id of the shipment the note is for
        :param tag: a tag for the note
        :param body: the content of the note
        :return: the created note, { "tag": "the tag", "body": "the body" }
        """

        data = {
            'body': body
        }

        if tag:
            data.update({'tag': tag})

        return self.api.post(shipment_notes_path(shipment_id), data=data)

    def get_notes(self, shipment_id):
        return self.api.get(shipment_notes_path(shipment_id))

    def get_note(self, shipment_id, note_id):
        return self.api.get(shipment_notes_path(shipment_id, note_id))

    def update_note(self, shipment_id, note_id, body, tag=None):
        """
        :param shipment_id: id of the shipment the note is for
        :param tag: a tag for the note
        :param body: the content of the note
        :return: the created note, { "tag": "the tag", "body": "the body" }
        """

        data = {
            body: body
        }

        if tag:
            data.update({'tag': tag})

        return self.api.post(shipment_notes_path(shipment_id, note_id), data=data)

    def delete_note(self, shipment_id, note_id):
        return self.api.delete(shipment_notes_path(shipment_id, note_id))
