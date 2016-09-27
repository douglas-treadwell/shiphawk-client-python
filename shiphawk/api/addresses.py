from .paths import addresses_path, address_code_path


class AddressesApi(object):
    def __init__(self, api):
        self.api = api

    def get(self, address_id=None):
        return self.api.get(addresses_path(address_id))

    def get_by_code(self, code):
        return self.api.get(address_code_path(code))

    def create(self, details):
        return self.api.post(addresses_path(), data=details)

    def update(self, details):
        if 'id' not in details.keys():
            raise ValueError("Update method expects an address with an id.")

        return self.api.post(addresses_path(details['id']), data=details)

    def delete(self, address_id):
        return self.api.delete(addresses_path(address_id))
