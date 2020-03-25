"""
Unit testing for carmd module in ../carmd
"""

from functools import wraps
import os
from pathlib import Path
import sys
import unittest
os.chdir(Path(__file__).parent)
os.chdir('../carmd')
sys.path.append(os.getcwd())  # required for relative file fetching - run in 'test' directory
from carmd import CarMD


class TestCarMD(unittest.TestCase):
    AUTHORIZATION = 'Basic MmE0MzBkZjYtOTIxOS00ODhjLTllMjktNjQ2MDlhMmY1OWZi'
    PARTNER_TOKEN = 'e18dc0f62dfb456398c83b893d3e81e1'
    vin = "1GNALDEK9FZ108495"
    year = 2015
    make = "chevrolet"
    model = "equinox"
    engine = "L4,2.4L;DOHC;16V;DI;FFV"
    mileage = 125000
    dtc = "p0420"

    def setUp(self):
        # comment out if you want to view instance influence on methods
        self.carmd = CarMD(self.AUTHORIZATION, self.PARTNER_TOKEN)

    def str_wrap(method):
        @wraps(method)
        def wrapper(inst, *args, **kwargs):
            vin, make = method(inst, *args, **kwargs)
            inst.assert_dict(vin, make)

        return wrapper

    def assert_dict(self, param1, param2):
        self.assertIsInstance(param1, dict)
        self.assertIsInstance(param2, dict)

    @str_wrap
    def test_fields(self):
        return self.carmd.fields.vin(self.vin),\
               self.carmd.fields.make(self.year, self.make, self.model, self.mileage)

    #
    # def test_decode(self):
    #     result_vin = self.carmd.decode.vin(self.vin)
    #     self.assertIsInstance(result_vin, dict)
    #
    # def test_obd2(self):
    #     result_vin = self.carmd.obd2.vin(self.vin)
    #     result_make = self.carmd.obd2.make(self.year, self.make, self.model)
    #     self.assertIsInstance(result_vin, dict)
    #     self.assertIsInstance(result_make, dict)
    #
    # def test_maintenance(self):
    #     result_vin = self.carmd.maintenance.vin(self.vin, self.mileage)
    #     result_make = self.carmd.maintenance.make(self.year, self.make, self.model, self.mileage)
    #     self.assertIsInstance(result_vin, dict)
    #     self.assertIsInstance(result_make, dict)
    #
    # def test_maintenance_list(self):
    #     result_vin = self.carmd.maintenance_list.vin(self.vin)
    #     result_make = self.carmd.maintenance_list.make(self.year, self.make, self.model)
    #     self.assertIsInstance(result_vin, dict)
    #     self.assertIsInstance(result_make, dict)
    #
    # def test_repair(self):
    #     result_vin = self.carmd.repair.vin(self.vin, self.mileage, self.dtc)
    #     self.assertIsInstance(result_vin, dict)
    #
    # def test_diagnostics(self):
    #     result_vin = self.carmd.diagnostics.vin(self.vin, self.mileage, self.dtc)
    #     self.assertIsInstance(result_vin, dict)
    #
    # def test_future_repairs(self):
    #     result_vin = self.carmd.future_repairs.vin(self.vin, self.mileage)
    #     result_make = self.carmd.future_repairs.make(self.year, self.make, self.model, self.mileage)
    #     self.assertIsInstance(result_vin, dict)
    #     self.assertIsInstance(result_make, dict)
    #
    # def test_tech_service(self):
    #     result_vin = self.carmd.tech_service.vin(self.vin)
    #     result_make = self.carmd.tech_service.make(self.year, self.make, self.model, self.engine)
    #     self.assertIsInstance(result_vin, dict)
    #     self.assertIsInstance(result_make, dict)
    #
    # def test_recalls(self):
    #     result_vin = self.carmd.recalls.vin(self.vin)
    #     result_make = self.carmd.recalls.make(self.year, self.make, self.model)
    #     self.assertIsInstance(result_vin, dict)
    #     self.assertIsInstance(result_make, dict)
    #
    # def test_warranty(self):
    #     result_vin = self.carmd.warranty.vin(self.vin)
    #     result_make = self.carmd.warranty.make(self.year, self.make, self.model)
    #     self.assertIsInstance(result_vin, dict)
    #     self.assertIsInstance(result_make, dict)
    #
    # def test_vehicle_image(self):
    #     result_vin = self.carmd.vehicle_image.vin(self.vin)
    #     self.assertIsInstance(result_vin, dict)
    #
    # def test_year(self):
    #     result = self.carmd.ymme.year()
    #     self.assertIsInstance(result, dict)
    #
    # def test_make(self):
    #     result = self.carmd.ymme.make(self.year)
    #     self.assertIsInstance(result, dict)
    #
    # def test_model(self):
    #     result = self.carmd.ymme.model(self.year, self.make)
    #     self.assertIsInstance(result, dict)
    #
    # def test_engine(self):
    #     result = self.carmd.ymme.engine(self.year, self.make, self.model)
    #     self.assertIsInstance(result, dict)
    #
    # def test_credits(self):
    #     result = self.carmd.acct_credit.balance()
    #     self.assertIsInstance(result, dict)

    def test_non_instance(self):
        with self.assertRaises(TypeError):
            CarMD()


if __name__ == '__main__':
    unittest.main()