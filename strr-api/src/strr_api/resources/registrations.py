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
from http import HTTPStatus
from io import BytesIO

from flasgger import swag_from
from flask import Blueprint, g, jsonify, request, send_file
from flask_cors import cross_origin
from werkzeug.utils import secure_filename

from strr_api.common.auth import jwt
from strr_api.exceptions import (
    AuthException,
    ExternalServiceException,
    ValidationException,
    error_response,
    exception_response,
)
from strr_api.requests import RegistrationRequest
from strr_api.responses import Document, Registration
from strr_api.schemas.utils import validate
from strr_api.services import AuthService, GCPStorageService, RegistrationService
from strr_api.validators.DocumentUploadValidator import validate_document_upload
from strr_api.validators.RegistrationRequestValidator import validate_registration_request

logger = logging.getLogger("api")
bp = Blueprint("registrations", __name__)


@bp.route("", methods=("GET",))
@swag_from({"security": [{"Bearer": []}]})
@cross_origin(origin="*")
@jwt.requires_auth
def get_registrations():
    """
    Get registrations for current user.
    ---
    tags:
      - registration
    responses:
      201:
        description:
      401:
        description:
    """

    try:
        registrations = RegistrationService.list_registrations(g.jwt_oidc_token_info)
        return (
            jsonify([Registration.from_db(registration).model_dump(mode="json") for registration in registrations]),
            HTTPStatus.OK,
        )
    except AuthException as auth_exception:
        return exception_response(auth_exception)


@bp.route("", methods=("POST",))
@swag_from({"security": [{"Bearer": []}]})
@cross_origin(origin="*")
@jwt.requires_auth
def create_registration():
    """
    Create a STRR registration.
    ---
    tags:
      - registration
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
      400:
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

        validate_registration_request(selected_account, registration_request)

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


@bp.route("/<registration_id>/documents", methods=("POST",))
@swag_from({"security": [{"Bearer": []}]})
@cross_origin(origin="*")
@jwt.requires_auth
def upload_registration_supporting_document(registration_id):
    """
    Upload a supporting document for a STRR registration.
    ---
    tags:
      - registration
    parameters:
          - in: path
            name: registration_id
            type: integer
            required: true
            description: ID of the registration
          - name: file
            in: formData
            type: file
            required: true
            description: The file to upload
    consumes:
      - multipart/form-data
    responses:
      201:
        description:
      400:
        description:
      401:
        description:
      403:
        description:
    """

    try:
        file = validate_document_upload(request.files)

        # only allow upload for registrations that belong to the user
        registration = RegistrationService.get_registration(g.jwt_oidc_token_info, registration_id)
        if not registration:
            raise AuthException()

        filename = secure_filename(file.filename)

        document = RegistrationService.save_registration_document(
            registration.eligibility.id, filename, file.content_type, file.read()
        )
        return jsonify(Document.from_db(document).model_dump(mode="json")), HTTPStatus.CREATED
    except AuthException as auth_exception:
        return exception_response(auth_exception)
    except ValidationException as auth_exception:
        return exception_response(auth_exception)
    except ExternalServiceException as service_exception:
        return exception_response(service_exception)


@bp.route("/<registration_id>/documents", methods=("GET",))
@swag_from({"security": [{"Bearer": []}]})
@cross_origin(origin="*")
@jwt.requires_auth
def get_registration_supporting_documents(registration_id):
    """
    Get registration supporting documents for given registration id.
    ---
    tags:
      - registration
    parameters:
          - in: path
            name: registration_id
            type: integer
            required: true
            description: ID of the registration
    responses:
      200:
        description:
      401:
        description:
      403:
        description:
    """

    try:
        # only allow upload for registrations that belong to the user
        registration = RegistrationService.get_registration(g.jwt_oidc_token_info, registration_id)
        if not registration:
            raise AuthException()

        documents = RegistrationService.get_registration_documents(registration_id)
        return (
            jsonify([Document.from_db(document).model_dump(mode="json") for document in documents]),
            HTTPStatus.OK,
        )
    except AuthException as auth_exception:
        return exception_response(auth_exception)


@bp.route("/<registration_id>/documents/<document_id>", methods=("GET",))
@swag_from({"security": [{"Bearer": []}]})
@cross_origin(origin="*")
@jwt.requires_auth
def get_registration_supporting_document_by_id(registration_id, document_id):
    """
    Get registration supporting document metadata for given registration id and document id.
    ---
    tags:
      - registration
    parameters:
          - in: path
            name: registration_id
            type: integer
            required: true
            description: ID of the registration
          - in: path
            name: document_id
            type: integer
            required: true
            description: ID of the document
    responses:
      200:
        description:
      401:
        description:
      403:
        description:
      404:
        description:
    """

    try:
        # only allow upload for registrations that belong to the user
        registration = RegistrationService.get_registration(g.jwt_oidc_token_info, registration_id)
        if not registration:
            raise AuthException()

        document = RegistrationService.get_registration_document(registration_id, document_id)
        if not document:
            return error_response(HTTPStatus.NOT_FOUND, "Document not found")

        return jsonify(Document.from_db(document).model_dump(mode="json")), HTTPStatus.OK
    except AuthException as auth_exception:
        return exception_response(auth_exception)


@bp.route("/<registration_id>/documents/<document_id>/file", methods=("GET",))
@swag_from({"security": [{"Bearer": []}]})
@cross_origin(origin="*")
@jwt.requires_auth
def get_registration_file_by_id(registration_id, document_id):
    """
    Get registration file contents for given registration id and document id.
    ---
    tags:
      - registration
    parameters:
          - in: path
            name: registration_id
            type: integer
            required: true
            description: ID of the registration
          - in: path
            name: document_id
            type: integer
            required: true
            description: ID of the document
    responses:
      200:
        description:
      401:
        description:
      403:
        description:
      404:
        description:
    """

    try:
        # only allow upload for registrations that belong to the user
        registration = RegistrationService.get_registration(g.jwt_oidc_token_info, registration_id)
        if not registration:
            raise AuthException()

        document = RegistrationService.get_registration_document(registration_id, document_id)
        if not document:
            return error_response(HTTPStatus.NOT_FOUND, "Document not found")

        file_bytes = GCPStorageService.fetch_registration_document(document.path)
        return send_file(
            BytesIO(file_bytes), as_attachment=True, download_name=document.file_name, mimetype=document.file_type
        )
    except AuthException as auth_exception:
        return exception_response(auth_exception)
    except ExternalServiceException as external_exception:
        return exception_response(external_exception)


@bp.route("/<registration_id>/documents/<document_id>", methods=("DELETE",))
@swag_from({"security": [{"Bearer": []}]})
@cross_origin(origin="*")
@jwt.requires_auth
def delete_registration_supporting_document_by_id(registration_id, document_id):
    """
    Delete registration supporting document for given registration id and document id.
    ---
    tags:
      - registration
    parameters:
          - in: path
            name: registration_id
            type: integer
            required: true
            description: ID of the registration
          - in: path
            name: document_id
            type: integer
            required: true
            description: ID of the document
    responses:
      204:
        description:
      401:
        description:
      403:
        description:
    """

    try:
        # only allow upload for registrations that belong to the user
        registration = RegistrationService.get_registration(g.jwt_oidc_token_info, registration_id)
        if not registration:
            raise AuthException()

        RegistrationService.delete_registration_document(registration_id, document_id)
        return "", HTTPStatus.NO_CONTENT
    except AuthException as auth_exception:
        return exception_response(auth_exception)
    except ExternalServiceException as external_exception:
        return exception_response(external_exception)
