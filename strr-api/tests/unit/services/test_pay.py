# Copyright © 2024 Province of British Columbia
#
# Licensed under the BSD 3 Clause License, (the "License");
# you may not use this file except in compliance with the License.
# The template for the license can be found here
#    https://opensource.org/license/bsd-3-clause/
#
# Redistribution and use in source and binary forms,
# with or without modification, are permitted provided that the
# following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS”
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
"""Tests to assure the pay service."""
import json
import os
from unittest.mock import patch

from strr_api import requests
from strr_api.services import PayService, RegistrationService, strr_pay
from tests.unit.utils.mocks import fake_user_from_token

REGISTRATION_MINIMUM_FIELDS = "registration_use_sbc_account_minimum"
MOCK_ACCOUNT_MINIMUM_FIELDS_REQUEST = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), f"../../mocks/json/{REGISTRATION_MINIMUM_FIELDS}.json"
)


def test_init(app):
    """Assure the init works as expected."""
    mock_svc_url = "https://fakeurl1"
    mock_timeout = 99
    mock_payload = {"wewa": {"lala"}}
    app.config.update(PAYMENT_SVC_URL=mock_svc_url)
    app.config.update(PAY_API_TIMEOUT=mock_timeout)
    new_pay = PayService(app=app, default_invoice_payload=mock_payload)

    assert new_pay.app == app
    assert new_pay.svc_url == mock_svc_url
    assert new_pay.timeout == mock_timeout
    assert new_pay.default_invoice_payload == mock_payload


def test_init_strr_pay(app):
    """Assure the init_app works as expected on strr_pay."""
    mock_svc_url = "https://fakeurl1"
    mock_timeout = 97
    app.config.update(PAYMENT_SVC_URL=mock_svc_url)
    app.config.update(PAY_API_TIMEOUT=mock_timeout)
    strr_pay.init_app(app)

    assert strr_pay.app == app
    assert strr_pay.svc_url == mock_svc_url
    assert strr_pay.timeout == mock_timeout
    assert strr_pay.default_invoice_payload == {
        "businessInfo": {"corpType": "STRR"},
        "filingInfo": {"filingTypes": [{"filingTypeCode": "RENTAL_FEE"}]},
        "paymentInfo": {"methodOfPayment": "DIRECT_PAY"},
    }


@patch("strr_api.models.user.User.get_or_create_user_by_jwt", new=fake_user_from_token)
def test_create_invoice(app, jwt, mocker, requests_mock):
    """Assure the create_invoice works as expected in strr_pay."""

    def mock_get_token():
        return "token"

    mocker.patch.object(jwt, "get_token_auth_header", mock_get_token)
    mock_json = {"id": "1234"}
    pay_api_mock = requests_mock.post(f"{app.config.get('PAYMENT_SVC_URL')}/payment-requests", json=mock_json)
    strr_pay.init_app(app)

    with open(MOCK_ACCOUNT_MINIMUM_FIELDS_REQUEST) as f:
        registration_data = json.load(f)

    registration_request = requests.RegistrationRequest(**registration_data)
    registration = RegistrationService.save_registration(None, 1000, registration_request.registration)
    invoice = strr_pay.create_invoice(jwt, 3299, registration)
    assert invoice.invoice_id == 1234
    assert invoice.payment_account == "3299"

    assert pay_api_mock.called
    payload = pay_api_mock.request_history[0].json()
    assert payload.get("filingInfo", {}).get("filingTypes") == [{"filingTypeCode": "RENTAL_FEE"}]
    assert payload.get("businessInfo", {}).get("corpType") == "STRR"
