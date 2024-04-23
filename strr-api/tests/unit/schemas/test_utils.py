from strr_api.schemas import utils
from strr_api.services.json_schema import SchemaService

# Replace path_to_schema_file, valid_json_data and invalid_json_data with actual test values
valid_json_data = {}
invalid_json_data = {}

schemas_path = SchemaService.scripts_directory()


def test_get_schema_store():
    schema_store = utils.get_schema_store()

    assert schema_store is not None
    assert isinstance(schema_store, dict)
