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
"""For a successfully paid registration, this service determines its auto-approval state."""
from flask import current_app

from strr_api.services.geocoder_service import GeoCoderService
from strr_api.services.ltsa_service import LtsaService
from strr_api.models.dss import DSSOrganization
from strr_api.responses.LTSAResponse import LtsaResponse
from strr_api.responses.AutoApprovalResponse import AutoApproval

class ApprovalService:
    """
    A class that provides utility functions for granting provisional or automatic approval
    """
    @classmethod
    def extract_longitude_and_latitude(cls, geocode_response):
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
    def build_ltsa_response(cls, ltsa_response):
        fielded_data = ltsa_response.get("order", {}).get("orderedProduct", {}).get("fieldedData", {})
        if fielded_data:
            ltsa_response = LtsaResponse(**fielded_data)
            return ltsa_response
        else:
            return None
        
    def check_full_name_exists_in_ownership_groups(ltsa_response: LtsaResponse, full_name: str) -> bool:
        full_name_parts = full_name.split()
        if len(full_name_parts) < 2:
            return False
        first_name = ' '.join(full_name_parts[:-1]).upper()
        last_name = full_name_parts[-1].upper()
        for ownership_group in ltsa_response.ownershipGroups:
            for title_owner in ownership_group.titleOwners:
                if title_owner.lastNameOrCorpName1.upper() == last_name and first_name in title_owner.givenName.upper():
                    return True
        return False
        
    #def process_approval(self, registration: models.Registration):
    @classmethod
    def process_approval(cls, pid: str, owner_name: str, address: str, renting: bool, other_service_provider: bool, pr_exempt: bool, bn_provided: bool, bcsc_address: str):
        """Process approval logic and produce output JSON to store in the DB and providing to FE"""

        # Status setting just temporary for visibility
        auto_approval = AutoApproval()

        try:
            if renting:
                auto_approval.renting = True
                auto_approval.status_to_set = "Full Review"
                return auto_approval
            else:
                auto_approval.renting = False
                if other_service_provider:
                    auto_approval.service_provider = True
                    auto_approval.status_to_set = "Full Review"
                    return auto_approval
                else:
                    auto_approval.service_provider = False

                if not pr_exempt:
                    auto_approval.pr_exempt = False
                    geocode_response = GeoCoderService.get_geocode_by_address(address)
                    longitude, latitude = cls.extract_longitude_and_latitude(geocode_response)
                    organization = DSSOrganization.lookup_by_geocode(longitude, latitude)
                    if organization["is_business_licence_required"]:
                        auto_approval.business_license_required = True
                        if bn_provided:
                            auto_approval.business_license_required_provided = True
                        else:
                            auto_approval.business_license_required_not_provided = True
                            auto_approval.status_to_set = "Full Review"
                            return auto_approval
                    else:
                        auto_approval.business_license_not_required_not_provided = True

                    ltsa_data = LtsaService.get_title_details_from_pid(pid)
                    ltsa_response = cls.build_ltsa_response(ltsa_data)
                    owner_title_match = cls.check_full_name_exists_in_ownership_groups(ltsa_response, owner_name)
                    if owner_title_match:
                        auto_approval.title_check = True
                        auto_approval.status_to_set = "Provisional Approval"
                    else:
                        auto_approval.title_check = False
                        auto_approval.status_to_set = "Full Review"
                    return auto_approval
                else:
                    if address != bcsc_address:
                        auto_approval.address_match = False
                        auto_approval.status_to_set = "Full Review"
                        return auto_approval
                    else:
                        auto_approval.address_match = True
                        geocode_response = GeoCoderService.get_geocode_by_address(address)
                        longitude, latitude = cls.extract_longitude_and_latitude(geocode_response)
                        organization = DSSOrganization.lookup_by_geocode(longitude, latitude)
                        if organization["is_principal_residence_required"]:
                            auto_approval.pr_exempt = False
                            auto_approval.status_to_set = "Full Review"
                        else:
                            auto_approval.pr_exempt = True
                            auto_approval.status_to_set = "Automatic Approval"
                        return auto_approval
        except Exception as default_exception:  # noqa: B902; log error
            current_app.logger.error("error in approval logoic:" + repr(default_exception))
            current_app.logger.error(auto_approval)
            return auto_approval