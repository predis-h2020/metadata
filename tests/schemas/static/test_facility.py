import pytest
import jsonschema
import os
import json

def test_facility():

    # path to facility metadata example file
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    facility_path = os.path.join(ROOT_DIR, '..', '..', '..', 'examples','static','facility.json' ) 
    facility = json.loads(open(facility_path).read())
    
    # path to schema file
    schema_path = os.path.join(ROOT_DIR, '..', '..', '..', 'schemas','static','facility.json' ) 
    schema = json.loads(open(schema_path).read())

    try:
    # validate data against schema
      jsonschema.validate(facility, schema)
      assert True, f"The data is valid according to the schema."
    except jsonschema.exceptions.ValidationError as e:
      assert False, f"The data is not valid. {e}"
    except jsonschema.exceptions.SchemaError as e:
      assert False, f"The schema is not valid. {e}"

    