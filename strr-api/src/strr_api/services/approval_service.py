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

# pylint: disable=R0914
# pylint: disable=R0912
# pylint: disable=R0915
"""For a successfully paid registration, this service determines its auto-approval state."""
from flask import current_app

from strr_api import models
from strr_api.common.utils import compare_addresses
from strr_api.enums.enum import EventRecordType, OwnershipType, RegistrationStatus
from strr_api.models import db
from strr_api.responses.AutoApprovalResponse import AutoApproval
from strr_api.responses.LTSAResponse import LtsaResponse
from strr_api.services import AuthService, EventRecordsService, LtsaService
from strr_api.services.geocoder_service import GeoCoderService


class ApprovalService:
    """
    A class that provides utility functions for granting provisional or automatic approval
    """

    @classmethod
    def extract_longitude_and_latitude(cls, geocode_response):
        """Extract longitude and latitude from the geocode response."""
        features = geocode_response.get("features", [])
        if features:
            first_feature = features[0]
            geometry = first_feature.get("geometry", {})
            coordinates = geometry.get("coordinates", [])
            if len(coordinates) == 2:
                longitude, latitude = coordinates
                return longitude, latitude
            else:
                return None, None
        else:
            return None, None

    @classmethod
    def check_full_name_exists_in_ownership_groups(cls, ltsa_response: LtsaResponse, full_name: str) -> bool:
        """Check if the full name exists in the ownership groups."""
        full_name_parts = full_name.split()
        if len(full_name_parts) < 2:
            return False
        first_name = " ".join(full_name_parts[:-1]).upper()
        last_name = full_name_parts[-1].upper()
        for ownership_group in ltsa_response.ownershipGroups:
            for title_owner in ownership_group.titleOwners:
                if title_owner.lastNameOrCorpName1.upper() == last_name and first_name in title_owner.givenName.upper():
                    return True
        return False

    @classmethod
    def process_approval(cls, token, registration: models.Registration):
        """Process approval logic and produce output JSON to store in the DB and providing to FE"""
        pid = registration.rental_property.parcel_identifier
        owner_name = (
            registration.rental_property.property_manager.primary_contact.firstname
            + " "
            + registration.rental_property.property_manager.primary_contact.lastname
        )
        address = (
            registration.rental_property.address.street_address
            + (
                " " + registration.rental_property.address.street_address_additional
                if registration.rental_property.address.street_address_additional
                else ""
            )
            + ", "
            + registration.rental_property.address.city
            + ", "
            + registration.rental_property.address.province
        )

        renting = registration.rental_property.ownership_type == OwnershipType.RENT.name
        other_service_provider = registration.eligibility.specified_service_provider is not None
        pr_exempt = not registration.eligibility.is_principal_residence
        bl_provided = registration.rental_property.local_business_licence is not None
        bcsc_address = AuthService.get_sbc_accounts_mailing_address(token, registration.sbc_account_id)

        # Status setting just temporary for visibility
        auto_approval = AutoApproval()

        try:
            if renting:
                auto_approval.renting = True
                registration.status = RegistrationStatus.UNDER_REVIEW
                registration.save()
                EventRecordsService.save_event_record(
                    EventRecordType.AUTO_APPROVAL_FULL_REVIEW,
                    EventRecordType.AUTO_APPROVAL_FULL_REVIEW.value,
                    True,
                    registration.user_id,
                    registration.id,
                )
                return auto_approval
            else:
                auto_approval.renting = False
                if other_service_provider:
                    auto_approval.service_provider = True
                    registration.status = RegistrationStatus.UNDER_REVIEW
                    registration.save()
                    EventRecordsService.save_event_record(
                        EventRecordType.AUTO_APPROVAL_FULL_REVIEW,
                        EventRecordType.AUTO_APPROVAL_FULL_REVIEW.value,
                        True,
                        registration.user_id,
                        registration.id,
                    )
                    return auto_approval
                else:
                    auto_approval.service_provider = False

                if not pr_exempt:
                    auto_approval.pr_exempt = False
                    if not compare_addresses(registration.rental_property.address, bcsc_address):
                        auto_approval.address_match = False
                        registration.status = RegistrationStatus.UNDER_REVIEW
                        registration.save()
                        EventRecordsService.save_event_record(
                            EventRecordType.AUTO_APPROVAL_FULL_REVIEW,
                            EventRecordType.AUTO_APPROVAL_FULL_REVIEW.value,
                            True,
                            registration.user_id,
                            registration.id,
                        )
                        return auto_approval
                    else:
                        auto_approval.address_match = True
                        geocode_response = GeoCoderService.get_geocode_by_address(address)
                        longitude, latitude = cls.extract_longitude_and_latitude(geocode_response)
                        organization = models.DSSOrganization.lookup_by_geocode(longitude, latitude)
                        if organization["is_business_licence_required"]:
                            auto_approval.business_license_required = True
                            if bl_provided:
                                auto_approval.business_license_required_provided = True
                            else:
                                auto_approval.business_license_required_not_provided = True
                                registration.status = RegistrationStatus.UNDER_REVIEW
                                registration.save()
                                EventRecordsService.save_event_record(
                                    EventRecordType.AUTO_APPROVAL_FULL_REVIEW,
                                    EventRecordType.AUTO_APPROVAL_FULL_REVIEW.value,
                                    True,
                                    registration.user_id,
                                    registration.id,
                                )
                                return auto_approval
                        else:
                            auto_approval.business_license_not_required_not_provided = True

                        if pid:
                            ltsa_data = LtsaService.get_title_details_from_pid(pid)
                            ltsa_response = LtsaService.build_ltsa_response(registration.id, ltsa_data)
                            owner_title_match = cls.check_full_name_exists_in_ownership_groups(
                                ltsa_response, owner_name
                            )
                        else:
                            owner_title_match = False
                        if owner_title_match:
                            auto_approval.title_check = True
                            registration.status = RegistrationStatus.PROVISIONAL
                            registration.save()
                            EventRecordsService.save_event_record(
                                EventRecordType.AUTO_APPROVAL_PROVISIONAL,
                                EventRecordType.AUTO_APPROVAL_PROVISIONAL.value,
                                True,
                                registration.user_id,
                                registration.id,
                            )
                        else:
                            auto_approval.title_check = False
                            registration.status = RegistrationStatus.UNDER_REVIEW
                            registration.save()
                            EventRecordsService.save_event_record(
                                EventRecordType.AUTO_APPROVAL_FULL_REVIEW,
                                EventRecordType.AUTO_APPROVAL_FULL_REVIEW.value,
                                True,
                                registration.user_id,
                                registration.id,
                            )
                        return auto_approval
                else:
                    geocode_response = GeoCoderService.get_geocode_by_address(address)
                    longitude, latitude = cls.extract_longitude_and_latitude(geocode_response)
                    organization = models.DSSOrganization.lookup_by_geocode(longitude, latitude)
                    if organization["is_principal_residence_required"]:
                        auto_approval.pr_exempt = False
                        registration.status = RegistrationStatus.UNDER_REVIEW
                        registration.save()
                        EventRecordsService.save_event_record(
                            EventRecordType.AUTO_APPROVAL_FULL_REVIEW,
                            EventRecordType.AUTO_APPROVAL_FULL_REVIEW.value,
                            True,
                            registration.user_id,
                            registration.id,
                        )
                    else:
                        auto_approval.pr_exempt = True
                        registration.status = RegistrationStatus.APPROVED
                        registration.save()
                        EventRecordsService.save_event_record(
                            EventRecordType.AUTO_APPROVAL_APPROVED,
                            EventRecordType.AUTO_APPROVAL_APPROVED.value,
                            True,
                            registration.user_id,
                            registration.id,
                        )
                    return auto_approval
        except Exception as default_exception:  # noqa: B902; log error
            current_app.logger.error("error in approval logoic:" + repr(default_exception))
            current_app.logger.error(auto_approval)
            return auto_approval

    @classmethod
    def save_approval_record(cls, registration_id, approval: AutoApproval):
        """Save approval record."""

        record = models.AutoApprovalRecord(registration_id=registration_id, record=approval.model_dump(mode="json"))
        db.session.add(record)
        db.session.commit()
        db.session.refresh(record)
        return record

    @classmethod
    def fetch_approval_records_for_registration(cls, registration_id):
        """Get approval records for a given registration by id."""
        query = models.AutoApprovalRecord.query.filter(models.AutoApprovalRecord.registration_id == registration_id)
        return query.all()
