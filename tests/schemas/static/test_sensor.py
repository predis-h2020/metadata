import pytest
import jsonschema
import os
import json

def test_sensor():

    # path to sensor metadata example file
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    sensor_path = os.path.join(ROOT_DIR, '..', '..', '..', 'examples','static','sensor.json' ) 
    sensor = json.loads(open(sensor_path).read())
    
    # path to schema file
    schema_path = os.path.join(ROOT_DIR, '..', '..', '..', 'schemas','static','sensor.json' ) 
    schema = json.loads(open(schema_path).read())

    try:
    # validate data against schema
      jsonschema.validate(sensor, schema)
      assert True, f"The data is valid according to the schema."
    except jsonschema.exceptions.ValidationError as e:
      assert False, f"The data is not valid. {e}"
    except jsonschema.exceptions.SchemaError as e:
      assert False, f"The schema is not valid. {e}"

    