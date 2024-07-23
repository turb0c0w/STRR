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

# pylint: disable=C0121

"""Logs Event Records to the Database."""
from strr_api import models
from strr_api.models import db


class EventRecordsService:
    """Service to save event records into the database."""

    @classmethod
    def save_event_record(
        cls, event_type: str, message: str, visible_to_end_user: bool, user_id: int = None, registration_id: int = None
    ):  # pylint: disable=R0913
        """Save STRR event record."""

        event_record = models.EventRecord(
            user_id=user_id,
            event_type=event_type.name,
            message=message,
            visible_to_end_user=visible_to_end_user,
            registration_id=registration_id,
        )
        db.session.add(event_record)
        db.session.commit()
        db.session.refresh(event_record)
        return event_record

    @classmethod
    def fetch_event_records_for_registration(cls, registration_id, only_show_visible_to_user: bool = True):
        """Get event records for a given registration by id."""
        query = models.EventRecord.query.filter(models.EventRecord.registration_id == registration_id)
        if only_show_visible_to_user:
            query = query.filter(models.EventRecord.visible_to_end_user == True)  # noqa
        return query.order_by(models.EventRecord.created_date).all()
