"""
EventRecord response object.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from strr_api.enums.enum import EventRecordType
from strr_api import models


class EventRecord(BaseModel):
    """EventRecord response object."""

    registration_id: Optional[int] = None
    event_type: str
    message: str
    created_date: datetime
    user_id: Optional[int] = None

    @classmethod
    def from_db(cls, source: models.EventRecord):
        """Return an EventRecord object from a database model."""
        return cls(
            registration_id=source.registration_id,
            event_type=source.event_type.name,
            message=source.message,
            created_date=source.created_date,
            user_id=source.user_id,
        )
