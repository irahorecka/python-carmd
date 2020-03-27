import json
import requests


def api_method(method):
    """Decorator for using method signatures for generating url endpoint."""
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        api = self.api
        vehicle = self.vehicle
        vehicle_id = '&'.join(['{}={}'.format(key, value) for key, value in vehicle.items() if value])
        if not vehicle_id:
            endpoint = api
        else:
            endpoint = '{}?{}'.format(api, vehicle_id)
        response = self.get(endpoint)

        return response

    return wrapper


class BaseAPI():
    """Base wraper for individual CarMD requests."""
    base_url = 'http://api.carmd.com/v3.0'
    api_header = {
        "content-type": "application/json",
        "authorization": "your_auth_key_here",
        "partner-token": "your_partner_token_here"
    }

    def __init__(self, auth, partner, **kwargs):
        """Initialize with appropriate authorization and partner-token for API header"""
        if not auth:
            raise KeyError("Please pass a valid authorization key: "
                           "e.g. 'Basic MmE0MzBkZjYtOTIxOS00ODhjLTllMjktNjQ2MDlhMmY1OWZx'")
        if not partner:
            raise KeyError("Please pass a valid partner-token key: "
                           "e.g. 'e18dc0f62dfb456398c83b893d3e81e2'")
        self.api_header["authorization"] = auth
        self.api_header["partner-token"] = partner
        self.kwargs = kwargs

    def get(self, endpoint):
        """Get request from specified url endpoint."""
        url = '{}/{}'.format(self.base_url, endpoint)
        response = requests.get(url, headers=self.api_header)
        if response.status_code != 200:
            raise ConnectionError("Bad request: {}".format(response.status_code))
        response_json = json.loads(response.content)

        return response_json


class FieldsVin(BaseAPI):
    """API for available fields under VIN:
    http://api.carmd.com/v3.0/fields"""
    api = 'fields'

    @api_method
    def __call__(self, mileage=None, dtc=None):
        self.vehicle = self.kwargs['vehicle']
        self.vehicle['mileage'] = mileage
        self.vehicle['dtc'] = dtc


class FieldsMake(BaseAPI):
    """API for available fields under make:
    http://api.carmd.com/v3.0/fields"""
    api = 'fields'

    @api_method
    def __call__(self, mileage=None):
        self.vehicle = self.kwargs['vehicle']
        self.vehicle['mileage'] = mileage


class Decode(BaseAPI):
    """API for VIN decode:
    http://api.carmd.com/v3.0/decode"""
    api = 'decode'

    @api_method
    def __call__(self):
        self.vehicle = self.kwargs['vehicle']


class DecodeEnhanced(BaseAPI):
    """
    Coming soon - to be an enhanced version
    of VIN decode.
    """
    # api = 'decode_enh'
    pass


class OBDPortLocation(BaseAPI):
    """API for finding OBD2 port location:
    http://api.carmd.com/v3.0/port"""
    api = 'port'

    @api_method
    def __call__(self):
        self.vehicle = self.kwargs['vehicle']


class Maintenance(BaseAPI):
    """API for maintenance:
    http://api.carmd.com/v3.0/maint"""
    api = 'maint'

    @api_method
    def __call__(self, mileage):
        self.vehicle = self.kwargs['vehicle']
        self.vehicle['mileage'] = mileage


class MaintenanceList(BaseAPI):
    """API for full maintenance list:
    http://api.carmd.com/v3.0/maintlist"""
    api = 'maintlist'

    @api_method
    def __call__(self):
        self.vehicle = self.kwargs['vehicle']


class Repairs(BaseAPI):
    """API for repair information:
    http://api.carmd.com/v3.0/repair"""
    api = 'repair'

    @api_method
    def __call__(self, mileage, dtc):
        self.vehicle = self.kwargs['vehicle']
        self.vehicle['mileage'] = mileage
        self.vehicle['dtc'] = dtc


class Diagnostics(BaseAPI):
    """API for diagnostic information:
    http://api.carmd.com/v3.0/diag"""
    api = 'diag'

    @api_method
    def __call__(self, mileage, dtc):
        self.vehicle = self.kwargs['vehicle']
        self.vehicle['mileage'] = mileage
        self.vehicle['dtc'] = dtc


class UpcomingRepairs(BaseAPI):
    """API for upcoming repairs:
    http://api.carmd.com/v3.0/upcoming"""
    api = 'upcoming'

    @api_method
    def __call__(self, mileage):
        self.vehicle = self.kwargs['vehicle']
        self.vehicle['mileage'] = mileage


class TSBVin(BaseAPI):
    """API for technical service bulletin using VIN:
    http://api.carmd.com/v3.0/tsb"""
    api = 'tsb'

    @api_method
    def __call__(self):
        self.vehicle = self.kwargs['vehicle']


class TSBMake(BaseAPI):
    """API for technical service bulletin using make:
    http://api.carmd.com/v3.0/tsb"""
    api = 'tsb'

    @api_method
    def __call__(self, engine):
        self.vehicle = self.kwargs['vehicle']
        self.vehicle['engine'] = engine


class SafetyRecalls(BaseAPI):
    """API for safety recalls:
    http://api.carmd.com/v3.0/recall"""
    api = 'recall'

    @api_method
    def __call__(self):
        self.vehicle = self.kwargs['vehicle']


class VehicleWarranty(BaseAPI):
    """API for warranty status:
    http://api.carmd.com/v3.0/warranty"""
    api = 'warranty'

    @api_method
    def __call__(self):
        self.vehicle = self.kwargs['vehicle']


class VehicleImage(BaseAPI):
    """API for getting vehicle image:
    http://api.carmd.com/v3.0/image"""
    api = 'image'

    @api_method
    def __call__(self):
        self.vehicle = self.kwargs['vehicle']


class YMME(BaseAPI):
    """API for getting year, model, make, and engine:
    http://api.carmd.com/v3.0/year
    http://api.carmd.com/v3.0/make
    http://api.carmd.com/v3.0/model
    http://api.carmd.com/v3.0/engine"""
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
    """API for account credits:
    http://api.carmd.com/v3.0/credits"""
    api = 'credits'

    @api_method
    def __call__(self):
        self.vehicle = {}


class CarMD():
    """General class for the CarMD API"""
    def __init__(self, auth_key=None, partner_key=None):
        self.args = (auth_key, partner_key)
        self.ymme = YMME(*self.args)
        self.acct_credits = Credits(*self.args)
        self.__vehicle = {}

    def __str__(self):
        return "CarMD Object - Vehicle ID: {}".format(self.__vehicle)

    def vin(self, vin):
        """Assign a VIN to the CarMD() instance"""
        self.my_vehicle = {
            'vin': vin}
        self.__vehicle = self.my_vehicle
        self.instantiate(vehicle=self.my_vehicle)
        return self

    def make(self, year, make, model):
        """Assign a make to the CarMD() instance"""
        self.my_vehicle = {
            'year': int(year),
            'make': make.upper(),
            'model': model.upper()
        }
        self.__vehicle = self.my_vehicle
        self.instantiate(vehicle=self.my_vehicle)
        return self

    def instantiate(self, **kwargs):
        """Instantiate appropriate classes by VIN or make"""
        if 'vin' in kwargs['vehicle']:
            self.fields = FieldsVin(*self.args, **kwargs)
            self.tech_service = TSBVin(*self.args, **kwargs)
            self.decode = Decode(*self.args, **kwargs)
            self.decode_enhanced = DecodeEnhanced(*self.args, **kwargs)
            self.repairs = Repairs(*self.args, **kwargs)
            self.diagnostics = Diagnostics(*self.args, **kwargs)
            self.vehicle_image = VehicleImage(*self.args, **kwargs)
        else:
            self.fields = FieldsMake(*self.args, **kwargs)
            self.tech_service = TSBMake(*self.args, **kwargs)
        self.obd2 = OBDPortLocation(*self.args, **kwargs)
        self.maintenance = Maintenance(*self.args, **kwargs)
        self.maintenance_list = MaintenanceList(*self.args, **kwargs)
        self.future_repairs = UpcomingRepairs(*self.args, **kwargs)
        self.recalls = SafetyRecalls(*self.args, **kwargs)
        self.warranty = VehicleWarranty(*self.args, **kwargs)
