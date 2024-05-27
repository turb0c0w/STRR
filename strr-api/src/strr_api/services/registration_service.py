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
from strr_api import models, requests
from strr_api.enums.enum import RegistrationStatus
from strr_api.models import db


class RegistrationService:
    """Service to save and load regristration details from the database."""

    @classmethod
    def save_registration(cls, jwt_oidc_token_info, sbc_account_id, registration_request: requests.Registration):
        """Save STRR property registration to database."""

        # TODO: FUTURE SPRINT - handle the other cases where jwt doesn't have the info
        user = models.User.get_or_create_user_by_jwt(jwt_oidc_token_info)
        user.email = registration_request.primaryContact.details.emailAddress
        user.preferredname = registration_request.primaryContact.details.preferredName
        user.phone_extension = registration_request.primaryContact.details.extension
        user.fax_number = registration_request.primaryContact.details.faxNumber
        user.phone_number = registration_request.primaryContact.details.phoneNumber
        user.date_of_birth = registration_request.primaryContact.dateOfBirth

        primary_contact = user
        db.session.add(primary_contact)
        db.session.flush()
        db.session.refresh(primary_contact)

        if registration_request.secondaryContact:
            secondary_contact = models.User(
                firstname=registration_request.secondaryContact.name.firstName,
                lastname=registration_request.secondaryContact.name.lastName,
                middlename=registration_request.secondaryContact.name.middleName,
                email=registration_request.secondaryContact.details.emailAddress,
                preferredname=registration_request.secondaryContact.details.preferredName,
                phone_extension=registration_request.secondaryContact.details.extension,
                fax_number=registration_request.secondaryContact.details.faxNumber,
                phone_number=registration_request.secondaryContact.details.phoneNumber,
                date_of_birth=registration_request.secondaryContact.dateOfBirth,
            )
            db.session.add(secondary_contact)
            db.session.flush()
            db.session.refresh(secondary_contact)

        property_manager = models.PropertyManager(
            user_id=primary_contact.id,
            secondary_contact_user_id=secondary_contact.id if secondary_contact else None,
            primary_address=models.Address(
                country=registration_request.primaryContact.mailingAddress.country,
                street_address=registration_request.primaryContact.mailingAddress.address,
                street_address_additional=registration_request.primaryContact.mailingAddress.addressLineTwo,
                city=registration_request.primaryContact.mailingAddress.city,
                province=registration_request.primaryContact.mailingAddress.province,
                postal_code=registration_request.primaryContact.mailingAddress.postalCode,
            ),
            secondary_address=models.Address(
                country=registration_request.secondaryContact.mailingAddress.country,
                street_address=registration_request.secondaryContact.mailingAddress.address,
                street_address_additional=registration_request.secondaryContact.mailingAddress.addressLineTwo,
                city=registration_request.secondaryContact.mailingAddress.city,
                province=registration_request.secondaryContact.mailingAddress.province,
                postal_code=registration_request.secondaryContact.mailingAddress.postalCode,
            )
            if secondary_contact
            else None,
        )
        db.session.add(property_manager)
        db.session.flush()
        db.session.refresh(property_manager)

        registration = models.Registration(
            sbc_account_id=sbc_account_id,
            status=RegistrationStatus.PENDING,
            rental_property=models.RentalProperty(
                property_manager_id=property_manager.id,
                address=models.Address(
                    country=registration_request.unitAddress.country,
                    street_address=registration_request.unitAddress.address,
                    street_address_additional=registration_request.unitAddress.addressLineTwo,
                    city=registration_request.unitAddress.city,
                    province=registration_request.unitAddress.province,
                    postal_code=registration_request.unitAddress.postalCode,
                ),
                nickname=registration_request.unitAddress.nickname,
                parcel_identifier=registration_request.unitDetails.parcelIdentifier,
                local_business_licence=registration_request.unitDetails.businessLicense,
                property_type=registration_request.unitDetails.propertyType,
                ownership_type=registration_request.unitDetails.ownershipType,
                rental_platforms=[
                    models.RentalPlatform(url=listing.url) for listing in registration_request.listingDetails
                ],
            ),
        )

        db.session.add(registration)
        db.session.commit()
        db.session.refresh(registration)
        return registration

    @classmethod
    def list_registrations(cls, jwt_oidc_token_info):
        """List all registrations for current user."""
        user = models.User.find_by_jwt_token(jwt_oidc_token_info)
        return (
            models.Registration.query.join(
                models.PropertyManager, models.PropertyManager.id == models.Registration.rental_property_id
            )
            .filter_by(user_id=user.id)
            .all()
        )
