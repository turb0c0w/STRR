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
"""Manages Auth service interactions."""
import requests
from flask import current_app

from strr_api.enums.enum import EventRecordType
from strr_api.requests.SBCAccountCreationRequest import SBCAccountCreationRequest
from strr_api.services.event_records_service import EventRecordsService
from strr_api.services.rest_service import RestService


class AuthService:
    """Service to invoke Rest calls to auth-api."""

    @classmethod
    def get_service_client_token(cls):
        """Get service account client token for cross api calls."""

        client_id = current_app.config.get("STRR_SERVICE_ACCOUNT_CLIENT_ID")
        client_secret = current_app.config.get("STRR_SERVICE_ACCOUNT_SECRET")
        token_url = current_app.config.get("KEYCLOAK_AUTH_TOKEN_URL")
        timeout = int(current_app.config.get("AUTH_SVC_TIMEOUT", 20))

        data = "grant_type=client_credentials"

        # get service account token
        res = requests.post(
            url=token_url,
            data=data,
            headers={"content-type": "application/x-www-form-urlencoded"},
            auth=(client_id, client_secret),
            timeout=timeout,
        )

        try:
            return res.json().get("access_token")
        except Exception:
            return None

    @classmethod
    def search_accounts(cls, account_name: str):
        """Search for accounts."""

        token = AuthService.get_service_client_token()
        endpoint = f"{current_app.config.get('AUTH_SVC_URL')}/orgs?name={account_name.strip()}"
        accounts = RestService.get(endpoint=endpoint, token=token).json()
        return accounts

    @classmethod
    def get_user_accounts(cls, bearer_token):
        """Return accounts for current user."""

        endpoint = f"{current_app.config.get('AUTH_SVC_URL')}/users/orgs"
        user_account_details = RestService.get(endpoint=endpoint, token=bearer_token).json()
        return user_account_details

    @classmethod
    def get_user_profile(cls, bearer_token):
        """Return current user profile."""

        endpoint = f"{current_app.config.get('AUTH_SVC_URL')}/users/@me"
        user_profile = RestService.get(endpoint=endpoint, token=bearer_token).json()
        return user_profile

    @classmethod
    def get_user_settings(cls, bearer_token, uuid):
        """Return a user's settings."""

        endpoint = f"{current_app.config.get('AUTH_SVC_URL')}/users/{uuid}/settings"
        user_settings = RestService.get(endpoint=endpoint, token=bearer_token).json()
        return user_settings

    @classmethod
    def create_user_account(cls, bearer_token, name, user_id):
        """Create a new user account."""

        endpoint = f"{current_app.config.get('AUTH_SVC_URL')}/orgs"
        create_account_payload = {
            "name": name,
            "accessType": "REGULAR",
            "typeCode": "BASIC",
            "productSubscriptions": [{"productCode": "STRR"}],
            "paymentInfo": {"paymentMethod": "DIRECT_PAY"},
            # "mailingAddress": mailing_address,
        }
        new_user_account = RestService.post(
            data=create_account_payload,
            endpoint=endpoint,
            token=bearer_token,
            generate_token=False,
        ).json()

        EventRecordsService.save_event_record(
            EventRecordType.SBC_ACCOUNT_CREATE, f'SBC Account Created: "{name}"', user_id
        )
        return new_user_account

    @classmethod
    def add_contact_info(cls, bearer_token, account_id, request: SBCAccountCreationRequest, user_id):
        """Create contact info for user account."""

        endpoint = f"{current_app.config.get('AUTH_SVC_URL')}/orgs/{account_id}/contacts"
        create_account_contact_payload = {
            "email": str(request.email),
            "phone": str(request.phone),
        }
        if request.phoneExtension:
            create_account_contact_payload["phoneExtension"] = str(request.phoneExtension)

        contact_info = RestService.post(
            data=create_account_contact_payload,
            endpoint=endpoint,
            token=bearer_token,
            generate_token=False,
        ).json()

        EventRecordsService.save_event_record(
            EventRecordType.SBC_ACCOUNT_ADDED_CONTACT, f'Added contact info to SBC account id: "{account_id}"', user_id
        )
        return contact_info
