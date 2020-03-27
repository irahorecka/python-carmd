"""
Unit testing for carmd module in ../carmd
"""

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

    def test_fields_vin(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.fields(self.mileage, self.dtc), dict)

    def test_fields_make(self):
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.fields(), dict)
        self.assertIsInstance(vehicle_make.fields(self.mileage), dict)
        with self.assertRaises(TypeError):
            vehicle_make.fields(self.mileage, dtc=self.dtc), dict

    def test_decode(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.decode(), dict)

    def test_obd2_vin(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.obd2(), dict)

    def test_obd2_make(self):
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.obd2(), dict)

    def test_maintenance_vin(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.maintenance(self.mileage), dict)
        with self.assertRaises(TypeError):
            vehicle_vin.maintenance()

    def test_maintenance_make(self):
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.maintenance(self.mileage), dict)
        with self.assertRaises(TypeError):
            vehicle_make.maintenance()

    def test_maintenance_list_vin(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.maintenance_list(), dict)

    def test_maintenance_list_make(self):
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.maintenance_list(), dict)

    def test_repair(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.repairs(mileage=self.mileage, dtc=self.dtc), dict)
        with self.assertRaises(TypeError):
            vehicle_vin.repairs()
        with self.assertRaises(TypeError):
            vehicle_vin.repairs(mileage=self.mileage)
        with self.assertRaises(TypeError):
            vehicle_vin.repairs(dtc=self.dtc)

    def test_diagnostics(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.diagnostics(mileage=self.mileage, dtc=self.dtc), dict)
        with self.assertRaises(TypeError):
            vehicle_vin.diagnostics()
        with self.assertRaises(TypeError):
            vehicle_vin.diagnostics(mileage=self.mileage)
        with self.assertRaises(TypeError):
            vehicle_vin.diagnostics(dtc=self.dtc)

    def test_future_repairs_vin(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.future_repairs(mileage=self.mileage), dict)
        with self.assertRaises(TypeError):
            vehicle_vin.future_repairs()

    def test_future_repairs_make(self):
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.future_repairs(mileage=self.mileage), dict)
        with self.assertRaises(TypeError):
            vehicle_make.future_repairs()

    def test_tech_service_vin(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.tech_service(), dict)

    def test_tech_service_make(self):
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.tech_service(engine=self.engine), dict)
        with self.assertRaises(TypeError):
            vehicle_make.tech_service()

    def test_recalls_vin(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.recalls(), dict)

    def test_recalls_make(self):
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.recalls(), dict)

    def test_warranty_vin(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.warranty(), dict)

    def test_warranty_make(self):
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.warranty(), dict)

    def test_vehicle_image(self):
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.vehicle_image(), dict)

    def test_year(self):
        self.assertIsInstance(self.carmd.ymme.year(), dict)
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.ymme.year(), dict)
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.ymme.year(), dict)

    def test_make(self):
        self.assertIsInstance(self.carmd.ymme.make(self.year), dict)
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.ymme.make(self.year), dict)
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.ymme.make(self.year), dict)

    def test_model(self):
        self.assertIsInstance(self.carmd.ymme.model(self.year, self.make), dict)
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.ymme.model(self.year, self.make), dict)
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.ymme.model(self.year, self.make), dict)

    def test_engine(self):
        self.assertIsInstance(self.carmd.ymme.engine(self.year, self.make, self.model), dict)
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.ymme.engine(self.year, self.make, self.model), dict)
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.ymme.engine(self.year, self.make, self.model), dict)

    def test_credits(self):
        self.assertIsInstance(self.carmd.acct_credits(), dict)
        vehicle_vin = self.carmd.vin(self.vin)
        self.assertIsInstance(vehicle_vin.acct_credits(), dict)
        vehicle_make = self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(vehicle_make.acct_credits(), dict)

    def test_non_instance(self):
        with self.assertRaises(KeyError):
            CarMD()

    def test_partial_instance(self):
        with self.assertRaises(KeyError):
            CarMD('Basic MmE0MzBkZjYtOTIxOS00ODhjLTllMjktNjQ2MDlhMmY1OWZi')

    def test_connection_error(self):
        with self.assertRaises(ConnectionError):
            self.carmd.ymme.make(self.model)  # accepts self.year


if __name__ == '__main__':
    unittest.main()