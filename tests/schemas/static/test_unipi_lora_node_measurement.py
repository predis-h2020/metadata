import pytest
import jsonschema
import os
import json

def test_unipi_lora_node_measurement():

    # path to unipi_lora_node_measurement metadata example file
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    unipi_lora_node_measurement_path = os.path.join(ROOT_DIR, '..', '..', '..', 'examples','static','unipi_lora_node_measurement.json' ) 
    unipi_lora_node_measurement = json.loads(open(unipi_lora_node_measurement_path).read())
    
    # path to schema file
    schema_path = os.path.join(ROOT_DIR, '..', '..', '..', 'schemas','static','unipi_lora_node_measurement.json' ) 
    schema = json.loads(open(schema_path).read())

    try:
    # validate data against schema
      jsonschema.validate(unipi_lora_node_measurement, schema)
      assert True, f"The data is valid according to the schema."
    except jsonschema.exceptions.ValidationError as e:
      assert False, f"The data is not valid. {e}"
    except jsonschema.exceptions.SchemaError as e:
      assert False, f"The schema is not valid. {e}"

    