"""
ORM Mapping for LTSARecord Records
"""
from __future__ import annotations

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import text

from .db import db


class LTSARecord(db.Model):
    """LTSARecord Record"""

    __tablename__ = "ltsa"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registration_id = db.Column(db.Integer, db.ForeignKey("registrations.id"), nullable=False)
    record = db.Column(JSONB, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, server_default=text("(NOW())"))
