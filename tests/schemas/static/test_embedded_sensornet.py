import pytest
import jsonschema
import os
import json

def test_embedded_sensornet():

    # path to embedded_sensornet metadata example file
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    embedded_sensornet_path = os.path.join(ROOT_DIR, '..', '..', '..', 'examples','static','embedded_sensornet.json' ) 
    embedded_sensornet = json.loads(open(embedded_sensornet_path).read())
    
    # path to schema file
    schema_path = os.path.join(ROOT_DIR, '..', '..', '..', 'schemas','static','embedded_sensornet.json' )
    schema_folder = os.path.join(ROOT_DIR, '..', '..', '..', 'schemas','static/')
    schema = json.loads(open(schema_path).read())

    try:
    # validate data against schema
      jsonschema.validate(embedded_sensornet, schema, resolver=jsonschema.RefResolver(
            base_uri=f"file:{schema_folder}",
            referrer=schema,
            ))
      assert True, f"The data is valid according to the schema."
    except jsonschema.exceptions.ValidationError as e:
      assert False, f"The data is not valid. {e}"
    except jsonschema.exceptions.SchemaError as e:
      assert False, f"The schema is not valid. {e}"

    