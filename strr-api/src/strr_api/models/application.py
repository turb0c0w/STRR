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
"""Registration Application Model."""
from __future__ import annotations

import copy
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import backref

from strr_api.common.enum import auto
from strr_api.common.enum import BaseEnum
from strr_api.models.base_model import BaseModel
from .db import db


class Application(BaseModel):
    """Stores the STRR Applications."""

    class Status(BaseEnum):
        """Enum of the application statuses."""

        DRAFT = auto()  # pylint: disable=invalid-name
        SUBMITTED = auto()  # pylint: disable=invalid-name
        PAID = auto()  # pylint: disable=invalid-name
        APPROVED = auto()  # pylint: disable=invalid-name
        ADDITIONAL_INFO_REQUESTED = auto()  # pylint: disable=invalid-name
        UNDER_REVIEW = auto()  # pylint: disable=invalid-name
        REJECTED = auto()  # pylint: disable=invalid-name
        PROVISIONAL = auto()  # pylint: disable=invalid-name

    __tablename__ = "application"

    id = db.Column(db.Integer, primary_key=True)
    application_json = db.Column("application_json", JSONB, nullable=False)
    application_date = db.Column(
        "application_date", db.DateTime(timezone=True), server_default=func.now()  # pylint:disable=not-callable
    )  # pylint:disable=not-callable
    type = db.Column("type", db.String(50), nullable=False, index=True)
    status = db.Column("status", db.String(20), default=Status.DRAFT, index=True)
    decision_date = db.Column("decision_date", db.DateTime(timezone=True))

    # maps to invoice id created by the pay-api (used for getting receipt)
    invoice_id = db.Column(db.Integer, nullable=True)
    payment_status_code = db.Column("payment_status_code", db.String(50))
    payment_completion_date = db.Column("payment_completion_date", db.DateTime(timezone=True))
    payment_account = db.Column("payment_account", db.String(30))

    # Relationships
    registration_id = db.Column("registration_id", db.Integer, db.ForeignKey("registrations.id"), nullable=True)
    submitter_id = db.Column("submitter_id", db.Integer, db.ForeignKey("users.id"))
    reviewer_id = db.Column("reviewer_id", db.Integer, db.ForeignKey("users.id"), nullable=True)

    submitter = db.relationship(
        "User",
        backref=backref("submitter", uselist=False),
        foreign_keys=[submitter_id],
    )
    reviewer = db.relationship(
        "User",
        backref=backref("reviewer", uselist=False),
        foreign_keys=[reviewer_id],
    )
    registration = db.relationship(
        "Registration",
        backref=backref("registration", uselist=False),
        foreign_keys=[registration_id],
    )

    @classmethod
    def find_by_id(cls, application_id: int) -> Application | None:
        """Return the application by id."""
        return cls.query.filter_by(id=application_id).one_or_none()

    @classmethod
    def find_by_invoice_id(cls, invoice_id: int) -> Application | None:
        """Return the application by invoice id."""
        return cls.query.filter_by(invoice_id=invoice_id).one_or_none()

    @classmethod
    def find_by_user_and_account(cls, user_id, account_id) -> Application | None:
        """Return the application by user and account."""
        return cls.query.filter_by(submitter_id=user_id).filter_by(payment_account=account_id).all()


class ApplicationSerializer:
    """Serializer for application. Can convert to dict, string from application model."""

    @staticmethod
    def to_str(application: Application):
        """Return string representation of application model."""
        return str(ApplicationSerializer.to_dict(application))

    @staticmethod
    def to_dict(application: Application) -> dict:
        """Return the application object as a dict."""
        application_dict = copy.deepcopy(application.application_json)
        if not application_dict.get("header", None):
            application_dict["header"] = {}
        application_dict["header"]["id"] = application.id
        application_dict["header"]["name"] = application.type
        application_dict["header"]["paymentToken"] = application.invoice_id
        application_dict["header"]["paymentStatus"] = application.payment_status_code
        application_dict["header"]["paymentAccount"] = application.payment_account
        application_dict["header"]["status"] = application.status
        application_dict["header"]["applicationDateTime"] = application.application_date.isoformat()
        application_dict["header"]["decisionDate"] = (
            application.decision_date.isoformat() if application.decision_date else None
        )
        application_dict["header"]["submitter"] = {}
        if application.submitter_id:
            application_dict["header"]["submitter"]["username"] = application.submitter.username

            submitter_display_name = ""
            if application.submitter.firstname:
                submitter_display_name = f"{submitter_display_name}{application.submitter.firstname}"
            if application.submitter.lastname:
                submitter_display_name = f"{submitter_display_name} {application.submitter.lastname}"
            application_dict["header"]["submitter"]["displayName"] = submitter_display_name

        application_dict["header"]["reviewer"] = {}
        if application.reviewer_id:
            application_dict["header"]["reviewer"]["username"] = application.reviewer.username

            reviewer_display_name = ""
            if application.reviewer.firstname:
                reviewer_display_name = f"{reviewer_display_name}{application.reviewer.firstname}"
            if application.reviewer.lastname:
                reviewer_display_name = f"{reviewer_display_name} {application.reviewer.lastname}"
            application_dict["header"]["reviewer"]["displayName"] = reviewer_display_name

        return application_dict
