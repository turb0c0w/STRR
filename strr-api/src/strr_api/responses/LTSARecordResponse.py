"""
LTSARecord response object.
"""
from datetime import datetime

from pydantic import BaseModel

from strr_api import models
from strr_api.responses import LtsaResponse


class LTSARecord(BaseModel):
    """LTSARecord response object."""

    id: int
    registration_id: int
    record: LtsaResponse
    creation_date: datetime

    @classmethod
    def from_db(cls, source: models.LTSARecord):
        """Return an LTSARecord object from a database model."""
        return cls(
            id=source.id,
            registration_id=source.registration_id,
            record=LtsaResponse(**source.record),
            creation_date=source.creation_date,
        )
