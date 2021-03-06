def none_to_empty_string(value):
    if value is None:
        return ''
    else:
        return value


def items_path(sub_path=None):
    return 'items/%s' % none_to_empty_string(sub_path)


def categories_path(sub_path=None):
    return 'categories/%s' % none_to_empty_string(sub_path)


def products_path(sub_path=None):
    # in v3 was 'products/%s'
    return 'skus/%s' % none_to_empty_string(sub_path)


def rates_path(sub_path=None):
    return 'rates/%s' % none_to_empty_string(sub_path)


def shipments_path(sub_path=None):
    return 'shipments/%s' % none_to_empty_string(sub_path)


def external_shipments_path():
    return 'external_shipments'


def shipment_notes_path(shipment_id, note_id=None):
    if not note_id:
        return shipments_path('%s/notes' % shipment_id)
    else:
        return shipments_path('%s/notes/%s' % (shipment_id, note_id))


def shipment_tracking_path(shipment_id):
    return shipments_path('%s/tracking' % shipment_id)


def shipment_labels_path(shipment_id):
    return shipments_path('%s/labels' % shipment_id)


def shipment_commercial_invoice_path(shipment_id):
    return shipments_path('%s/commercial_invoice' % shipment_id)


def shipment_bill_of_lading_path(shipment_id):
    return shipments_path('%s/bol' % shipment_id)


def shipments_status_path():
    return shipments_path('status')


def notifications_path(sub_path=None):
    return 'notifications/%s' % none_to_empty_string(sub_path)


def catalog_sale_path(): # sale_notifications_path
    return notifications_path('catalog_sale')


def zip_codes_path(sub_path=None):
    return 'zip_codes/%s' % none_to_empty_string(sub_path)


def orders_path(sub_path=None):
    return 'orders/%s' % none_to_empty_string(sub_path)


def addresses_path(sub_path=None):
    return 'addresses/%s' % none_to_empty_string(sub_path)


def address_code_path(code):
    return addresses_path('code/%s' % none_to_empty_string(code))
