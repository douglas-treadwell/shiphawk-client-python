import requests

from ..errors import raise_error

from .products import ProductsApi
from .rates import RatesApi
from .orders import OrdersApi

from functools import wraps


def process_response(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        response = original_function(*args, **kwargs)

        if (response.status_code // 100) != 2:
            raise_error(response)

        try:
            return response.json()
        except ValueError:
            return response.content  # likely ""

    return wrapper


class Api(object):
    API_PATH = '/api/'

    def __init__(self, client):
        self.client = client

        self.base_url = client.host_url + Api.API_PATH + client.api_version + '/'

        self.http_headers = {
            'User-Agent': 'ShipHawk Client/0',
            'Accept': 'application/json',
            'X-API-KEY': client.api_token
        }

        self.products = ProductsApi(self)
        self.skus = self.products  # an alternative way to access the same api

        self.rates = RatesApi(self)
        self.orders = OrdersApi(self)

    # endpoint in all the below should be resource_path

    @process_response
    def get(self, endpoint, params=None, **kwargs):
        return requests.get(self.base_url + endpoint, params, headers=self.http_headers, **kwargs)

    @process_response
    def patch(self, endpoint, data=None, **kwargs):
        return requests.patch(self.base_url + endpoint, data, headers=self.http_headers, **kwargs)

    @process_response
    def put(self, endpoint, data=None, **kwargs):
        return requests.put(self.base_url + endpoint, data, headers=self.http_headers, **kwargs)

    @process_response
    def post(self, endpoint, data=None, json=None, **kwargs):
        return requests.post(self.base_url + endpoint, data=data, json=json, headers=self.http_headers, **kwargs)

    @process_response
    def delete(self, endpoint, **kwargs):
        return requests.delete(self.base_url + endpoint, headers=self.http_headers, **kwargs)

    def get_all(self, resource_path, per_request=100):
        page = 1
        collection = []

        while True:
            params = {'page': page,
                      'per_page': per_request,
                      'api_token': self.client.api_token}

            response = self.get(resource_path, params)
            collection.extend(response.json())

            if len(collection) >= response.headers['X-Total']:
                break

            page += 1

        return collection

    def get_by_id(self, resource_path, id):
        return self.get(resource_path + id)

    def get_with_options(self, resource_path, options):
        return self.get(resource_path, options)
