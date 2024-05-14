from http import HTTPStatus
from unittest.mock import patch

from tests.unit.utils.mocks import empty_json, no_op


@patch("strr_api.services.AuthService.get_service_client_token", new=no_op)
@patch("strr_api.services.PayService.get_fee_codes", new=empty_json)
def test_fee_codes_200(client):
    rv = client.get("/pay/fee_codes")
    assert rv.status_code == HTTPStatus.OK
