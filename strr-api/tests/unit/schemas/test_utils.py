from strr_api.schemas import utils


def test_get_schema():
    schema_store = utils.get_schema("new_account.json")
    assert schema_store is not None


def test_validate_schema():
    valid, error = utils.validate_schema({"name": "a"}, "new_account")
    assert valid
    assert not error


def test_validate_schema_error():
    valid, error = utils.validate_schema({"a": "b"}, "new_account")
    assert not valid
    assert error


def test_validate():
    valid, error = utils.validate({"name": "a"}, "new_account")
    assert valid
    assert not error
