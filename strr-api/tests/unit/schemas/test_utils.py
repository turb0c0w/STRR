import json
import os

from strr_api.schemas import utils

REGISTRATION = "registration"
MOCK_ACCOUNT_REQUEST = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), f"../../mocks/json/{REGISTRATION}.json"
)


def test_get_schema():
    schema_store = utils.get_schema(f"{REGISTRATION}.json")
    assert schema_store is not None


def test_validate_schema():
    with open(MOCK_ACCOUNT_REQUEST) as f:
        data = json.load(f)
        valid, error = utils.validate_schema(data, f"{REGISTRATION}")
        assert valid
        assert not error


def test_validate_schema_error():
    valid, error = utils.validate_schema({"a": "b"}, f"{REGISTRATION}")
    assert not valid
    assert error


def test_validate():
    with open(MOCK_ACCOUNT_REQUEST) as f:
        data = json.load(f)
        valid, error = utils.validate(data, f"{REGISTRATION}")
        assert valid
        assert not error
