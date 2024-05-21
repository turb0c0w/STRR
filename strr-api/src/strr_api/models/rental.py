"""This manages a Retal record 

"""
from __future__ import annotations

from flask import current_app
from sqlalchemy.orm import relationship

from .db import db


class RentalProperty(db.Model):

    __tablename__ = "rental_properties"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_manager_id = db.Column(db.Integer, db.ForeignKey('property_managers.id'), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    parcel_identifier = db.Column(db.String, nullable=True)
    local_business_licence = db.Column(db.String, nullable=True)
    # Enum: portion of principal residence, entire principal residence, secondary suit, accessory dwelling unit, investment property
    property_type = db.Column(db.String, nullable=False)
    ownership_type = db.Column(db.String, nullable=False)  # Enum: own, rent, co-own

    property_manager = relationship('PropertyManager', back_populates='rental_properties')
    rental_platforms = relationship('RentalPlatform', back_populates='rental_properties')


class Address(db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country = db.Column(db.String, nullable=False)
    street_address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    province = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.String, nullable=False)

    property_managers_primary = relationship(
        'PropertyManager', back_populates='primary_address', foreign_keys='PropertyManager.primary_address_id')
    property_managers_secondary = relationship(
        'PropertyManager', back_populates='secondary_address', foreign_keys='PropertyManager.secondary_address_id')


class PropertyManager(db.Model):
    __tablename__ = 'property_managers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    primary_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    secondary_address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=True)

    user = relationship('User', back_populates='property_managers')
    primary_address = relationship('Address', foreign_keys=[
                                   primary_address_id], back_populates='property_managers_primary')
    secondary_address = relationship('Address', foreign_keys=[
                                     secondary_address_id], back_populates='property_managers_secondary')


class RentalPlatform(db.Model):
    __tablename__ = 'rental_platforms'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('rental_properties.id'), nullable=False)
    url = db.Column(db.String, nullable=False)

    property = relationship('RentalProperty', back_populates='rental_platforms')
