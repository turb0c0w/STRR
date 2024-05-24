# Copyright © 2023 Province of British Columbia
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

"""
This module provides a simple flask blueprint with a single 'home' route that returns a JSON response.
"""

import logging
import re
from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, g, jsonify, request
from flask_cors import cross_origin

from strr_api.common.auth import jwt
from strr_api.exceptions import AuthException, ExternalServiceException, ValidationException, exception_response
from strr_api.requests import RegistrationRequest
from strr_api.responses import Registration
from strr_api.schemas.utils import validate

# from strr_api.schemas import utils as schema_utils
from strr_api.services import AuthService, RegistrationService

logger = logging.getLogger("api")
bp = Blueprint("account", __name__)


@bp.route("/me", methods=("GET",))
@swag_from({"security": [{"Bearer": []}]})
@cross_origin(origin="*")
@jwt.requires_auth
def me():
    """
    Get current user's profile.
    ---
    tags:
      - users
    responses:
      200:
        description:
      401:
        description:
    """
    try:
        token = jwt.get_token_auth_header()
        response = AuthService.get_user_accounts(token)
        profile = AuthService.get_user_profile(token)
        settings = AuthService.get_user_settings(token, profile["keycloakGuid"])
        response["profile"] = profile
        response["settings"] = settings
        return jsonify(response), HTTPStatus.OK
    except AuthException as auth_exception:
        return exception_response(auth_exception)
    except ExternalServiceException as service_exception:
        return exception_response(service_exception)


@bp.route("", methods=("POST",))
@swag_from({"security": [{"Bearer": []}]})
@cross_origin(origin="*")
@jwt.requires_auth
def create_account():
    """
    Create a new account for the user.
    ---
    tags:
      - users
    parameters:
          - in: body
            name: body
            schema:
              type: object
              required:
                - name
              properties:
                name:
                  type: string
                  description: The name of the new user account.
    responses:
      201:
        description:
      401:
        description:
    """

    try:
        token = jwt.get_token_auth_header()
        json_input = request.get_json()
        [valid, errors] = validate(json_input, "registration")
        if not valid:
            raise ValidationException(message=errors)

        registration_request = RegistrationRequest(**json_input)
        selected_account = registration_request.selectedAccount

        # SBC Account lookup or creation
        sbc_account_id = None
        if selected_account.sbc_account_id:
            sbc_account_id = selected_account.sbc_account_id
        else:
            new_account = AuthService.create_user_account(
                token, selected_account.name, selected_account.mailingAddress.to_dict()
            )
            sbc_account_id = new_account.get("id")

        # DO POSTAL CODE VALIDATION IF COUNTRY IS CANADA
        if selected_account.mailingAddress:
            selected_account.mailingAddress.postalCode = validate_and_format_canadian_postal_code(
                selected_account.mailingAddress.country,
                selected_account.mailingAddress.region,
                selected_account.mailingAddress.postalCode,
            )

        registration_request.registration.unitAddress.postalCode = validate_and_format_canadian_postal_code(
            registration_request.registration.unitAddress.country,
            registration_request.registration.unitAddress.province,
            registration_request.registration.unitAddress.postalCode,
        )

        if (
            registration_request.registration.unitAddress.country != "CA"
            or registration_request.registration.unitAddress.province != "BC"
        ):
            raise ValidationException(message="Invalid Rental Unit Address. Location must be in British Columbia.")

        registration_request.registration.primaryContact.mailingAddress.postalCode = (
            validate_and_format_canadian_postal_code(
                registration_request.registration.primaryContact.mailingAddress.country,
                registration_request.registration.primaryContact.mailingAddress.province,
                registration_request.registration.primaryContact.mailingAddress.postalCode,
            )
        )

        if registration_request.registration.secondaryContact:
            registration_request.registration.secondaryContact.mailingAddress.postalCode = (
                validate_and_format_canadian_postal_code(
                    registration_request.registration.secondaryContact.mailingAddress.country,
                    registration_request.registration.secondaryContact.mailingAddress.province,
                    registration_request.registration.secondaryContact.mailingAddress.postalCode,
                )
            )

        registration = RegistrationService.save_registration(
            g.jwt_oidc_token_info, sbc_account_id, registration_request.registration
        )
        return jsonify(Registration.from_db(registration).model_dump(mode="json")), HTTPStatus.CREATED
    except ValidationException as auth_exception:
        return exception_response(auth_exception)
    except AuthException as auth_exception:
        return exception_response(auth_exception)
    except ExternalServiceException as service_exception:
        return exception_response(service_exception)


def validate_and_format_canadian_postal_code(country: str, province: str, postal_code: str):
    """Validate and format a Canadian postal code."""

    if country == "CA":
        if province not in ["BC", "AB", "SK", "MB", "ON", "QC", "NB", "PE", "NS", "NL", "YT", "NT", "NU"]:
            raise ValidationException(
                message="Invalid province. Must be one of 'BC', 'AB', 'SK', 'MB', 'ON', 'QC', "
                + "'NB', 'PE', 'NS', 'NL', 'YT', 'NT', 'NU'"
            )

        regex = r"^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$"
        match = re.match(regex, postal_code)
        if match:
            return postal_code.upper().replace(" ", "")
        else:
            raise ValidationException(message="Invalid postal code. Must be in the format 'A1A 1A1' or 'A1A1A1'")

    return postal_code


# @bp.route("/search_accounts", methods=("GET",))
# @cross_origin(origin="*")
# def search_accounts():
#     """
#     search_accounts
#     ---
#     tags:
#       - users
#     responses:
#       200:
#         description:
#       401:
#         description:
#     """

#     try:
#         token = AuthService.search_accounts("test")
#         return jsonify({"token": token}), HTTPStatus.OK
#     except AuthException as auth_exception:
#         return exception_response(auth_exception)
#     except ExternalServiceException as service_exception:
#         return exception_response(service_exception)
