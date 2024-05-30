"""
Document response object.
"""
from pydantic import BaseModel

from strr_api import models


class Document(BaseModel):
    """Document response object."""

    registration_id: int
    document_id: int
    file_name: str
    file_type: str

    @classmethod
    def from_db(cls, source: models.Document):
        """Return a Document object from a database model."""
        return cls(
            registration_id=source.eligibility.registration_id,
            document_id=source.id,
            file_name=source.file_name,
            file_type=source.file_type,
        )
