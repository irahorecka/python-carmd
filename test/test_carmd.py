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
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.fields(self.mileage, self.dtc), dict)

    def test_fields_make(self):
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.fields(), dict)
        self.assertIsInstance(self.carmd.fields(self.mileage), dict)
        with self.assertRaises(TypeError):
            self.carmd.fields(self.mileage, dtc=self.dtc), dict

    def test_decode(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.decode(), dict)

    def test_obd2_vin(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.obd2(), dict)

    def test_obd2_make(self):
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.obd2(), dict)

    def test_maintenance_vin(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.maintenance(self.mileage), dict)
        with self.assertRaises(TypeError):
            self.carmd.maintenance()

    def test_maintenance_make(self):
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.maintenance(self.mileage), dict)
        with self.assertRaises(TypeError):
            self.carmd.maintenance()

    def test_maintenance_list_vin(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.maintenance_list(), dict)

    def test_maintenance_list_make(self):
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.maintenance_list(), dict)

    def test_repair(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.repairs(mileage=self.mileage, dtc=self.dtc), dict)
        with self.assertRaises(TypeError):
            self.carmd.repairs()
        with self.assertRaises(TypeError):
            self.carmd.repairs(mileage=self.mileage)
        with self.assertRaises(TypeError):
            self.carmd.repairs(dtc=self.dtc)

    def test_diagnostics(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.diagnostics(mileage=self.mileage, dtc=self.dtc), dict)
        with self.assertRaises(TypeError):
            self.carmd.diagnostics()
        with self.assertRaises(TypeError):
            self.carmd.diagnostics(mileage=self.mileage)
        with self.assertRaises(TypeError):
            self.carmd.diagnostics(dtc=self.dtc)

    def test_future_repairs_vin(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.future_repairs(mileage=self.mileage), dict)
        with self.assertRaises(TypeError):
            self.carmd.future_repairs()

    def test_future_repairs_make(self):
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.future_repairs(mileage=self.mileage), dict)
        with self.assertRaises(TypeError):
            self.carmd.future_repairs()

    def test_tech_service_vin(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.tech_service(), dict)

    def test_tech_service_make(self):
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.tech_service(engine=self.engine), dict)
        with self.assertRaises(TypeError):
            self.carmd.tech_service()

    def test_recalls_vin(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.recalls(), dict)

    def test_recalls_make(self):
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.recalls(), dict)

    def test_warranty_vin(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.warranty(), dict)

    def test_warranty_make(self):
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.warranty(), dict)

    def test_vehicle_image(self):
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.vehicle_image(), dict)

    def test_year(self):
        self.assertIsInstance(self.carmd.ymme.year(), dict)
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.ymme.year(), dict)
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.ymme.year(), dict)

    def test_make(self):
        self.assertIsInstance(self.carmd.ymme.make(self.year), dict)
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.ymme.make(self.year), dict)
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.ymme.make(self.year), dict)

    def test_model(self):
        self.assertIsInstance(self.carmd.ymme.model(self.year, self.make), dict)
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.ymme.model(self.year, self.make), dict)
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.ymme.model(self.year, self.make), dict)

    def test_engine(self):
        self.assertIsInstance(self.carmd.ymme.engine(self.year, self.make, self.model), dict)
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.ymme.engine(self.year, self.make, self.model), dict)
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.ymme.engine(self.year, self.make, self.model), dict)

    def test_credits(self):
        self.assertIsInstance(self.carmd.acct_credits(), dict)
        self.carmd.vin(self.vin)
        self.assertIsInstance(self.carmd.acct_credits(), dict)
        self.carmd.make(self.year, self.make, self.model)
        self.assertIsInstance(self.carmd.acct_credits(), dict)

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