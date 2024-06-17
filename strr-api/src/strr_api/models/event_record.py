"""
ORM Mapping for Event Records
"""
from __future__ import annotations

from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text

from strr_api.enums.enum import EventRecordType

from .db import db


class EventRecord(db.Model):
    """Event Record"""

    __tablename__ = "event_records"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    event_type = db.Column(Enum(EventRecordType), nullable=False)
    message = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, server_default=text("(NOW())"))

    user = relationship("User")
