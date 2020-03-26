python-carmd
================

A simple `CarMD <https://api.carmd.com/member/login>`__ API wrapper.

License: `MIT <https://en.wikipedia.org/wiki/MIT_License>`__.

Installation
------------

::

    pip install python-carmd

API Examples
------------
Make an instance of the ``CarMD`` class with your authorization and partner-token API keys. For example:

+---------------+--------------------------------------------------------+
| Authorization | Basic MmE0MzBkZjYtOTIxOS00ODhjLTllMjktNjQ2MDlhMmY1OWZi |
+---------------+--------------------------------------------------------+
| Partner-token | e18dc0f62dfb456398c83b893d3e81e1                       |
+---------------+--------------------------------------------------------+


.. code:: python

    from carmd import CarMD
    my_car = CarMD("Basic MmE0MzBkZjYtOTIxOS00ODhjLTllMjktNjQ2MDlhMmY1OWZi",
                   "e18dc0f62dfb456398c83b893d3e81e1")


Get available API fields for vehicle by VIN or make.

.. code:: python

    fields_vin = my_car.fields.vin('1GNALDEK9FZ108495')
    fields_make = my_car.fields.make(2015, 'Chevrolet', 'Equinox')

    # Output:
    {
      "message":{...},
      "data":{
        "decode":true,
        "port":true,
        "maint":false,
        "maintlist":true,
        "repair":false,
        "diag":false,
        "upcoming":false,
        "tsb":true,
        "recall":true,
        "warranty":false
      }
    }


Get information about your vehicle through VIN.

.. code:: python

    decode_vin = my_car.decode.vin('1GNALDEK9FZ108495')

    # Output:
    {
      "message":{...},
      "data":{
        "year":2015,
        "make":"CHEVROLET",
        "model":"EQUINOX",
        "manufacturer": "GENERAL MOTORS",
        "engine":" L4, 2.4L; DOHC; 16V; DI; FFV",
        "trim": "LTZ",
        "transmission": "AUTOMATIC"
      }
    }


Get information about your car's OBD2 port location.

.. code:: python

    obd_loc_vin = my_car.obd2.vin('1GNALDEK9FZ108495')
    obd_loc_make = my_car.obd2.make(2015, 'Chevrolet', 'Equinox')

    # Output:
    {
      "message":{...},
      "data":{
        "location_img": "http://api2.carmd.com/v2.0/Content/dlc/position/2.jpg"
        "location_value":2,
        "access_img":"https://secure-downloads.innova.com/dlc-location-images-wm/chevrolet/equinox/equinox-2-cmd.jpg?Expires=1529947955&Signature=YdnADor-AWZ6cIydvBLJNWuAc9Wi4axsmx1kmmgc3Wb~OZafjgRPpO7X1w0rbZm-BSh4a3byoAOmucKIVbrZoClcHrV0QZ6b58hum9w005Q-0YbUwcfentrcOkrT5VXM1sL-xe3~s-egf18TUciCX8oZBGh5RyLa9SFprEb74vfu9fpLpBxzqAN4n6mV2~z0WTfVjTVWPEVjoNEro2ro4EMP7LjpkKRf8KCGsTexCNkVh1P3MzvZcpDUV9TE9dfbltanvv9fVt9g12qU7GfoCTEZTCOnlkfUzaFTAcHOdnrQCDEp5m8ZVlAFrh104X4xHqWMZ3HnDySWoArAbnvpyA__&Key-Pair-Id=APKAJVI4C2YLKAQ7KO6A",
        "access_notes":"uncovered",
        "notes":"Driver Side - Under Lower Left Side of Dashboard"
      }
    }


Get your vehicle's maintenance information within +/- 10,000 miles of the submitted mileage.

.. code:: python

    maintenance_vin = my_car.maintenance.vin('1GNALDEK9FZ108495', 125000)
    maintenance_make = my_car.maintenance.make(2015, 'Chevrolet', 'Equinox', 125000)

    # Output:
    {
      "message":{...},
      "data":[{
        "desc":"Inspect For Fluid Leaks",
        "due_mileage":52500,
        "is_oem":True,
        "repair":{
          "repair_difficulty":2,
          "repair_hours":0.0,
          "labor_rate_per_hour":106.38,
          "part_cost":6.15,
          "labor_cost":0.0,
          "misc_cost":0.0,
          "total_cost":6.15
        },
        "parts":[{
          "desc":"Engine Oil",
          "manufacturer":"",
          "price":"6.15",
          "qty":"1"
        }]
      },
      {...}]
    }


Get the entire maintenance schedule of your vehicle.

.. code:: python

    maintenance_list_vin = my_car.maintenance_list.vin('1GNALDEK9FZ108495')
    maintenance_list_make = my_car.maintenance_list.make(2015, 'Chevrolet', 'Equinox')

    # Output:
    {
      "message":{...},
      "data":[{
        "desc": "Inspect Steering & Suspension Components",
        "due_mileage": 7500,
        "is_oem": true,
        "is_cycle": true,
        "cycle_mileage": 7500,
        "repair": {
          "repair_difficulty": 2,
          "repair_hours": 0,
          "labor_rate_per_hour": 101.44,
          "part_cost": 166.51,
          "labor_cost": 0,
          "misc_cost": 0,
          "total_cost": 166.51
        },
        "parts": [{
          "desc": "Steering Tie Rod End",
          "manufacturer": "",
          "price": 108.03,
          "qty": 1
        },{
          "desc": "Steering Tie Rod End",
          "manufacturer": "",
          "price": 58.48,
          "qty": 1
        }]
      },
      {...}]
    }


Get your vehicle's repair information from its VIN, mileage, and check engine light data.

.. code:: python

    repairs_vin = my_car.repairs.vin('1GNALDEK9FZ108495', 125000, 'p0420')

    # Output:
    {
      "message":{...},
      "data":[{
        "desc":"Replace Catalytic Converter(s) with new OE Catalytic Converter(s),
        "urgency":2,
        "urgency_desc":"Repair immediately if drivability issues are present. Threat to essential system components if not repaired as soon as possible.",
        "repair":{
          "difficulty":3,
          "hours":2.3,
          "labor_rate_per_hour":106.38,
          "part_cost":1967.01,
          "labor_cost":244.674,
          "misc_cost":25,
          "total_cost":2236.684
        },
        "parts":[{
          "desc":"Catalytic Converter",
          "manufacturer":"",
          "price":683.67,
          "qty":"1"
        },{
          "desc":"Catalytic Converter",
          "manufacturer":"",
          "price":1283.34,
          "qty":"1"
        }],
        "tsb":[{
          "id":118676,
          "manufacturer_number":"07-00-89-037K",
          "desc":"Warranty Administration - Courtesy Transportation and Roadside Assistance Programs",
          "categories":["Tools & Hardware"]
          "file_name":"4824780",
          "file_url":"http://downloads.innova.com/tsb-files/118000/4824780.pdf",
          "issue_date":"2017-06-23T00:00:00",
          "updated_date":"2017-10-10T00:00:00"
        },{...}]
      },
      {...}]
    }


Get your vehicle's diagnostic information from its VIN, mileage, and check engine light data.

.. code:: python

    diagnostics_vin = my_car.diagnostics.vin('1GNALDEK9FZ108495', 125000, 'p0420')
    {
      "message":{...},
      "data":{
        "code":"P0420",
        "urgency":2,
        "urgency_desc":"Repair immediately if drivability issues are present. Threat to essential system components if not repaired as soon as possible.",
        "effect_on_vehicle":"This condition will prevent the vehicle from running at its optimum efficiency and fuel economy may suffer.",
        "responsible_system":"Sensors indicate the catalytic converter is not reducing exhaust gas emissions properly.",
        "layman_definition":"Catalyst System Efficiency Below Threshold (Bank 1)",
        "tech_definition":"Catalyst System Low Efficiency (Bank 1)",
      }
    }


Get upcoming repairs for your vehicle up to 12 months by including your mileage.

.. code:: python

    future_repairs_vin = my_car.future_repairs.vin('1GNALDEK9FZ108495', 125000)
    future_repairs_make = my_car.future_repairs.make(2015, 'Chevrolet', 'Equinox', 125000)

    # Output:
    {
      "message":{...},
      "data":[{
        "desc":"Replace Camshaft Position (CMP) Actuator Solenoid",
        "probability":0.57,
        "hours":1.96,
        "part_cost":144.18,
        "labor_cost":208.9,
        "misc_cost":25.0,
        "total_cost":378.09
      },  {
        "desc":"Replace Variable Valve Timing (VVT) Solenoid",
        "probability":0.19,
        "hours":0.6,
        "part_cost":58.21,
        "labor_cost":63.82,
        "misc_cost":25.0,
        "total_cost":147.03
      },{...}]
    }


Get your vehicle's technical service bulletins (include engine if you are using make).

.. code:: python

    tsb_vin = my_car.tech_service.vin('1GNALDEK9FZ108495')
    tsb_make = my_car.tech_service.make(2015, 'Chevrolet', 'Equinox', 'L4,2.4L;DOHC;16V;DI;FFV')

    # Output:
    {
      "message":{...},
      "data":[{
        "id":118676,
        "manufacturer_number":"07-00-89-037K",
        "desc":"Warranty Administration - Courtesy Transportation and Roadside Assistance Programs",
        "categories":["Tools & Hardware"]
        "file_name":"4824780",
        "file_url":"http://downloads.innova.com/tsb-files/118000/4824780.pdf",
        "issue_date":"2017-06-23T00:00:00",
        "updated_date":"2017-10-10T00:00:00"
      },{
        "id":118672,
        "manufacturer_number":"15086A",
        "desc":"Customer Satisfaction - OnStar System Inoperative - Chip Corruption",
        "categories":["Recall"]
        "file_name":"4828709",
        "file_url":"http://downloads.innova.com/tsb-files/118000/4828709.pdf",
        "issue_date":"2017-06-22T00:00:00",
        "updated_date":"2017-10-10T00:00:00"
      },{...}]
    }


Get safety recalls on your vehicle.

.. code:: python

    recalls_vin = my_car.recalls.vin('1GNALDEK9FZ108495')
    recalls_make = my_car.recalls.make(2015, 'Chevrolet', 'Equinox')

    # Output:
    {
      "message":{...},
      "data":[{
        "desc":""GENERAL MOTORS LLC (GM) IS RECALLING CERTAIN MODEL YEAR 2015 BUICK LACROSSE, CADILLAC XTS, CHEVROLET CAMARO, EQUINOX, MALIBU, AND GMC TERRAIN VEHICLES.  THE AFFECTED VEHICLES HAVE FRONT SEAT-MOUNTED SIDE IMPACT AIR BAGS WHOSE INFLATOR MAY RUPTURE UPON ITS DEPLOYMENT.",
        "corrective_action":" GM WILL NOTIFY OWNERS, AND DEALERS WILL REPLACE THE SIDE IMPACT AIR BAG MODULES, FREE OF CHARGE. THE RECALL BEGAN ON OCTOBER 19, 2015.  OWNERS MAY CONTACT BUICK CUSTOMER SERVICE AT 1-800-521-7300, CHEVROLET CUSTOMER SERVICE AT 1-800-222-1020, CADILLAC CUSTOMER SERVICE AT 1-800-458-8006, OR GMC CUSTOMER SERVICE AT 1-800-462-8782.  GM'S NUMBER FOR THIS RECALL IS 01320.",
        "consequence":""IN THE EVENT OF A CRASH NECESSITATING DEPLOYMENT OF ONE OR BOTH OF THE SIDE IMPACT AIR BAGS, THE AIR BAG'S INFLATOR MAY RUPTURE AND THE AIR BAG MAY NOT PROPERLY INFLATE. THE RUPTURE COULD CAUSE METAL FRAGMENTS TO STRIKE THE VEHICLE OCCUPANTS, POTENTIALLY RESULTING IN SERIOUS INJURY OR DEATH.  ADDITIONALLY, IF THE AIR BAG DOES NOT PROPERLY INFLATE, THE DRIVER OR PASSENGER IS AT AN INCREASED RISK OF INJURY.",
        "recall_date":"1/16/2015",
        "campaign_number":"15V666000",
        "recall_number":"17668"
      },
      {...}]
    }


Get warranty status of your vehicle.

.. code:: python

    warranty_vin = my_car.warranty.vin('1GNALDEK9FZ108495')
    warranty_make = my_car.warranty.make(2015, 'Chevrolet', 'Equinox')

    # Output
    {
      "message":{...},
      "data":[{
        "type":"Electric/Hybrid",
        "criteria":"8 year / 100,000 miles ",
        "note":" Battery components only ",
        "max_miles":100000,
        "max_year ":8,
        "transferable":true
      },{
        "type":"Basic",
        "criteria":"3 year / 36,000 miles",
        "note":"",
        "max_miles":36000,
        "max_year ":3,
        "transferable":true
      },{...}]
    }


Get an image of your vehicle.

.. code:: python

    image_vin = my_car.vehicle_image.vin('1GNALDEK9FZ108495')

    # Output
    {
      "message":{...},
      "data":[{
        "image":"image_of_vehicle_here"
      }]
    }


Get assistance in identifying your car's year, make, model, and engine without using VIN.

.. code:: python

    vehicle_year = my_car.ymme.year()

    # Output
    {
      "message":{...},
      "data":[ "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005","2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996"]
    }


    vehicle_make = my_car.ymme.make(2015)

    # Output
    {
      "message":{...},
      "data":[ "ACURA", "Alfa Romeo", "Aston Martin", "Bently", "BMW", "Buick", "Cadillac", "Chevrolet", "Chrysler", "Dodge", "Ferrari", "Fiat", "Ford", "GMC","Honda", "Hyundai", "..."]
    }


    vehicle_model = my_car.ymme.model(2015, 'Chevrolet')

    # Output
    {
      "message":{...},
      "data":[ "ILX", "MDX", "RDX", "RLX", "TLX"]
    }


    vehicle_engine = my_car.ymme.engine(2015, 'Chevrolet', 'Equinox')

    # Output
    {
      "message":{...},
      "data":["V6, 3.5L; SOHC; 24V; SEFI","V6, 3.5L; SOHC; 24V; SEFI; Hybrid"]
    }


Get remaining credits on your account

.. code:: python

    credits = my_car.acct_credits.balance()

    # Output
    {
      "message":{...},
      "data":{
        "credits":1000
      }
    }


Support
-------
If you find any bug or you want to propose a new feature, please use the `issues tracker <https://github.com/irahorecka/python-carmd/issues>`__. I'll be happy to help!
