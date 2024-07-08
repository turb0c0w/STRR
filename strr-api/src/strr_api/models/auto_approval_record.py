"""
ORM Mapping for AutoApprovalRecord Records
"""
from __future__ import annotations

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import text

from .db import db


class AutoApprovalRecord(db.Model):
    """AutoApprovalRecord Record"""

    __tablename__ = "auto_approval_records"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registration_id = db.Column(db.Integer, db.ForeignKey("registrations.id"), nullable=False)
    record = db.Column(JSONB, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, server_default=text("(NOW())"))
