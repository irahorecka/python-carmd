import functools
import requests
import json
AUTHORIZATION = 'Basic MmE0MzBkZjYtOTIxOS00ODhjLTllMjktNjQ2MDlhMmY1OWZi'
PARTNER_TOKEN = 'e18dc0f62dfb456398c83b893d3e81e1'

class BaseAPI():
    base_url = 'http://api.carmd.com/v3.0'
    api_header = {
        "content-type": "application/json",
        "authorization": "your_auth_key_here",
        "partner-token": "your_partner_token_here"
    }

    def __init__(self, auth=AUTHORIZATION, partner=PARTNER_TOKEN):
        if not auth:
            raise KeyError("Please pass a valid authorization key.")
        if not partner:
            raise KeyError("Please pass a valid partner-token key")
        self.api_header["authorization"] = auth
        self.api_header["partner-token"] = partner

    def get(self, endpoint):
        url = f'{self.base_url}/{endpoint}'
        item = requests.get(url, headers=self.api_header)
        if item.status_code != 200:
            print('bad request')
        response = json.loads(item.content)

        return response


def api_method(method):
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        api = self.api
        vehicle = self.vehicle
        
        vehicle_id = '&'.join([f'{key}={value}' for key, value in vehicle.items() if value])
        print(vehicle_id)
        endpoint = f"{api}?{vehicle_id}"
        response = self.get(endpoint)
        
        return response

    return wrapper


def endpoint_generator(method):
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        print(kwargs, args)
        if method.__name__ == 'vin':
            self.vehicle = {
                'vin': self.vin_no,
                'mileage': self.mileage,
                'dtc': self.dtc
            }
        elif method.__name__ == 'make':
            self.vehicle = {
                'year': self.year,
                'make': self.manufacturer.lower(),
                'model': self.model.lower(),
                'mileage': self.mileage
            }

    return wrapper


class Fields(BaseAPI):
    api = 'fields'

    @api_method
    @endpoint_generator
    def vin(self, vin_no, mileage=None, dtc=None):
        self.vin_no = vin_no
        self.mileage = mileage
        self.dtc = dtc

    @api_method
    @endpoint_generator
    def make(self, year, manufacturer, model, mileage=None):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = mileage


class Decode(BaseAPI):
    api = 'decode'

    @api_method
    @endpoint_generator
    def vin(self, vin_no):
        self.vin_no = vin_no





if __name__ == '__main__':
    x = Fields()
    z = x.vin(vin_no='1GNALDEK9FZ108495')
    # y = x.get('fields')
    from pprint import pprint
    pprint(z)
    zz = x.make(2009, 'Toyota', 'priuS')
    pprint(zz)
    y = Decode()
    zzz = y.vin(vin_no='1GNALDEK9FZ108495')
    pprint(zzz)
