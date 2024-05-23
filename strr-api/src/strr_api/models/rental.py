"""This manages a Retal record

"""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import Enum
from sqlalchemy.orm import relationship

from strr_api.enums.enum import OwnershipType, PropertyType, RegistrationStatus

from .db import db


class RentalProperty(db.Model):
    """Rental Property"""

    __tablename__ = "rental_properties"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_manager_id = db.Column(db.Integer, db.ForeignKey("property_managers.id"), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"), nullable=False)
    nickname = db.Column(db.String, nullable=True)
    parcel_identifier = db.Column(db.String, nullable=True)
    local_business_licence = db.Column(db.String, nullable=True)
    # Enum: All or part of primary dwelling; Secondary suite; Accessory dwelling unit; Float home; Other
    property_type = db.Column(Enum(PropertyType), nullable=False)
    ownership_type = db.Column(Enum(OwnershipType), nullable=False)  # Enum: own, rent, co-own

    property_manager = relationship("PropertyManager")
    rental_platforms = relationship("RentalPlatform")
    registrations = relationship("Registration")
    address = relationship("Address", foreign_keys=[address_id], back_populates="rental_properties_address")


class Address(db.Model):
    """Address"""

    __tablename__ = "addresses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String, nullable=False)
    street_address = db.Column(db.String, nullable=False)
    street_address_additional = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=False)
    province = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.String, nullable=False)

    property_managers_primary = relationship(
        "PropertyManager", back_populates="primary_address", foreign_keys="PropertyManager.primary_address_id"
    )
    property_managers_secondary = relationship(
        "PropertyManager", back_populates="secondary_address", foreign_keys="PropertyManager.secondary_address_id"
    )
    rental_properties_address = relationship(
        "RentalProperty", back_populates="address", foreign_keys="RentalProperty.address_id"
    )


class PropertyManager(db.Model):
    """Property Manager"""

    __tablename__ = "property_managers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    secondary_contact_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    primary_address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"), nullable=False)
    secondary_address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"), nullable=True)

    primary_contact_user = relationship("User", foreign_keys=[user_id])
    secondary_contact_user = relationship("User", foreign_keys=[secondary_contact_user_id])
    primary_address = relationship(
        "Address", foreign_keys=[primary_address_id], back_populates="property_managers_primary"
    )
    secondary_address = relationship(
        "Address", foreign_keys=[secondary_address_id], back_populates="property_managers_secondary"
    )


class RentalPlatform(db.Model):
    """Rental Platform"""

    __tablename__ = "rental_platforms"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    property_id = db.Column(db.Integer, db.ForeignKey("rental_properties.id"), nullable=False)
    url = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=True)

    property = relationship("RentalProperty", back_populates="rental_platforms")


class Registration(db.Model):
    """Registration"""

    __tablename__ = "registrations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rental_property_id = db.Column(db.Integer, db.ForeignKey("rental_properties.id"), nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    status = db.Column(Enum(RegistrationStatus), nullable=False)  # Enum: pending, approved, more info needed, denied

    rental_property = relationship("RentalProperty", back_populates="registrations")
