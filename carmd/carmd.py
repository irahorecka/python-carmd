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
        response = requests.get(url, headers=self.api_header)
        if response.status_code != 200:
            raise ConnectionError(f"Bad request: {response.status_code}")
        response_json = json.loads(response.content)

        return response_json


def api_method(method):
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        api = self.api
        vehicle = self.vehicle
        vehicle_id = '&'.join([f'{key}={value}' for key, value in vehicle.items() if value])
        if not vehicle_id:
            endpoint = api
        else:
            endpoint = f"{api}?{vehicle_id}"
        response = self.get(endpoint)
        
        return response

    return wrapper


class Fields(BaseAPI):
    api = 'fields'

    @api_method
    def vin(self, vin_no, mileage=None, dtc=None):
        self.vehicle = {
            'vin': vin_no,
            'mileage': mileage,
            'dtc': dtc
        }

    @api_method
    def make(self, year, manufacturer, model, mileage=None):
        self.vehicle = {
            'year': year,
            'make': manufacturer.upper(),
            'model': model.upper(),
            'mileage': mileage
        }


class Decode(BaseAPI):
    api = 'decode'

    @api_method
    def vin(self, vin_no):
        self.vehicle = {
            'vin': vin_no
        }


class DecodeEnhanced(BaseAPI):
    """
    Coming soon - to be an enhanced version
    of VIN decode.
    """
    # api = 'decode_enh'
    pass


class OBDPortLocation(BaseAPI):
    api = 'port'

    @api_method
    def vin(self, vin_no):
        self.vehicle = {
            'vin': vin_no
        }

    @api_method
    def make(self, year, manufacturer, model):
        self.vehicle = {
            'year': year,
            'make': manufacturer.upper(),
            'model': model.upper()
        }


class Maintenance(BaseAPI):
    api = 'maint'

    @api_method
    def vin(self, vin_no, mileage):
        self.vehicle = {
            'vin': vin_no,
            'mileage': mileage
        }

    @api_method
    def make(self, year, manufacturer, model, mileage):
        self.vehicle = {
            'year': year,
            'make': manufacturer.upper(),
            'model': model.upper(),
            'mileage': mileage
        }


class Repair(BaseAPI):
    api = 'repair'

    @api_method
    def vin(self, vin_no, mileage, dtc):
        self.vehicle = {
            'vin': vin_no,
            'mileage': mileage,
            'dtc': dtc
        }


class Diagnostics(BaseAPI):
    api = 'diag'

    @api_method
    def vin(self, vin_no, mileage, dtc):
        self.vehicle = {
            'vin': vin_no,
            'mileage': mileage,
            'dtc': dtc
        }


class UpcomingRepairs(BaseAPI):
    api = 'upcoming'

    @api_method
    def vin(self, vin_no, mileage):
        self.vehicle = {
            'vin': vin_no,
            'mileage': mileage
        }

    @api_method
    def make(self, year, manufacturer, model, mileage):
        self.vehicle = {
            'year': year,
            'make': manufacturer.upper(),
            'model': model.upper(),
            'mileage': mileage
        }


class TSB(BaseAPI):
    api = 'tsb'

    @api_method
    def vin(self, vin_no):
        self.vehicle = {
            'vin': vin_no
        }

    @api_method
    def make(self, year, manufacturer, model, engine):
        self.vehicle = {
            'year': year,
            'make': manufacturer.upper(),
            'model': model.upper(),
            'engine': engine
        }


class SafetyRecalls(BaseAPI):
    api = 'recall'

    @api_method
    def vin(self, vin_no):
        self.vehicle = {
            'vin': vin_no
        }

    @api_method
    def make(self, year, manufacturer, model):
        self.vehicle = {
            'year': year,
            'make': manufacturer.upper(),
            'model': model.upper()
        }


class VehicleWarranty(BaseAPI):
    api = 'warranty'

    @api_method
    def vin(self, vin_no):
        self.vehicle = {
            'vin': vin_no
        }

    @api_method
    def make(self, year, manufacturer, model):
        self.vehicle = {
            'year': year,
            'make': manufacturer.upper(),
            'model': model.upper()
        }


class VehicleImage(BaseAPI):
    api = 'image'

    @api_method
    def vin(self, vin_no):
        self.vehicle = {
            'vin': vin_no
        }


class YMME(BaseAPI):
    @api_method
    def year(self):
        self.api = 'year'
        self.vehicle = {}

    @api_method
    def make(self, year):
        self.api = 'make'
        self.vehicle = {
            'year': year
        }

    @api_method
    def model(self, year, make):
        self.api = 'model'
        self.vehicle = {
            'year': year,
            'make': make.upper()
        }

    @api_method
    def engine(self, year, make, model):
        self.api = 'engine'
        self.vehicle = {
            'year': year,
            'make': make.upper(),
            'model': model.upper()
        }


class Credits(BaseAPI):
    api = 'credits'

    @api_method
    def balance(self):
        self.vehicle = {}


class CarMD():
    fields = None
    decode = None
    decode_enhanced = None
    obd2 = None
    maintenance = None
    repair = None
    diagnostics = None
    future_repairs = None
    tech_service = None
    recalls = None
    warranty = None
    vehicle_image = None
    ymme = None
    acct_credit = None

    def __init__(self):
        self.fields = Fields()
        self.decode = Decode()
        self.decode_enhanced = DecodeEnhanced()
        self.obd2 = OBDPortLocation()
        self.maintenance = Maintenance()
        self.repair = Repair()
        self.diagnostics = Diagnostics()
        self.future_repairs = UpcomingRepairs()
        self.tech_service = TSB()
        self.recalls = SafetyRecalls()
        self.warranty = VehicleWarranty()
        self.vehicle_image = VehicleImage()
        self.ymme = YMME()
        self.acct_credit = Credits()
        