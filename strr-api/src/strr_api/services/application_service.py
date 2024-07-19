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
"""Service to interact with the applications model."""
from datetime import datetime, timezone
from strr_api.enums.enum import ApplicationType
from strr_api.models import Application, User
from strr_api.models.application import ApplicationSerializer


class ApplicationService:
    """Service to interact with the applications model."""

    @staticmethod
    def serialize(application: Application) -> dict:
        """Returns application JSON."""
        return ApplicationSerializer.to_dict(application)

    @staticmethod
    def save_application(jwt_oidc_token_info, account_id, request_json: dict):
        """Saves an application to db."""
        user = User.get_or_create_user_by_jwt(jwt_oidc_token_info)
        if request_json.get("selectedAccount"):
            del request_json["selectedAccount"]
        application = Application()
        application.payment_account = account_id
        application.submitter = user
        application.type = ApplicationType.REGISTRATION.value
        application.application_json = request_json
        application.save()
        return application

    @staticmethod
    def list_applications(jwt_oidc_token_info, account_id):
        """List all applications for current user and account."""
        user = User.find_by_jwt_token(jwt_oidc_token_info)
        if not user:
            return []
        return Application.find_by_user_and_account(user.id, account_id)

    @staticmethod
    def get_application(jwt, account_id, application_id):
        """Get the application with the specified application id for the current user and account."""
        user = User.find_by_jwt_token(jwt)
        if not user:
            return None
        return Application.get_application(user.id, account_id, application_id)

    @staticmethod
    def update_application_payment_details_and_status(application: Application, invoice_details: dict) -> Application:
        """
        Updates the invoice details in the application. This method also updates the application status based on
        the invoice status.
        """
        application.invoice_id = invoice_details["id"]
        application.payment_account = invoice_details.get("paymentAccount").get("accountId")
        application.payment_status_code = invoice_details.get("statusCode")
        if application.payment_status_code == "COMPLETED":
            application.status = Application.Status.PAID
            application.payment_completion_date = datetime.fromisoformat(invoice_details.get("paymentDate"))
        elif application.payment_status_code == "APPROVED":
            application.payment_status_code = "COMPLETED"
            application.status = Application.Status.PAID
            application.payment_completion_date = datetime.now(timezone.utc)
        else:
            if application.status == Application.Status.DRAFT:
                application.status = Application.Status.SUBMITTED
        application.save()
        return application
