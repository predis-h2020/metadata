import pytest
import jsonschema
import os
import json

def test_unipi_lora_node():

    # path to unipi_lora_node metadata example file
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    unipi_lora_node_path = os.path.join(ROOT_DIR, '..', '..', '..', 'examples','static','unipi_lora_node.json' ) 
    unipi_lora_node = json.loads(open(unipi_lora_node_path).read())
    
    # path to schema file
    schema_path = os.path.join(ROOT_DIR, '..', '..', '..', 'schemas','static','unipi_lora_node.json' )
    schema_folder = os.path.join(ROOT_DIR, '..', '..', '..', 'schemas','static/')
    schema = json.loads(open(schema_path).read())

    try:
    # validate data against schema
      jsonschema.validate(unipi_lora_node, schema, resolver=jsonschema.RefResolver(
            base_uri=f"file:{schema_folder}",
            referrer=schema,
            ))
      assert True, f"The data is valid according to the schema."
    except jsonschema.exceptions.ValidationError as e:
      assert False, f"The data is not valid. {e}"
    except jsonschema.exceptions.SchemaError as e:
      assert False, f"The schema is not valid. {e}"

    