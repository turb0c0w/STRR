from strr_api.schemas import utils


def test_get_schema():
    schema_store = utils.get_schema('goodbye.json')
    assert schema_store is not None


def test_validate_exception():
    valid, error = utils.validate({"a": "b"}, 'garbage.json')
    assert not valid
    assert error
