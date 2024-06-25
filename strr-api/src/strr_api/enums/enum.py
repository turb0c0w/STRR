# Copyright © 2024 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Enum definitions."""

from enum import Enum


class AuthHeaderType(Enum):
    """Authorization header types."""

    BASIC = "Basic {}"
    BEARER = "Bearer {}"


class ContentType(Enum):
    """Http Content Types."""

    JSON = "application/json"
    FORM_URL_ENCODED = "application/x-www-form-urlencoded"
    PDF = "application/pdf"


class LoginSource(Enum):
    """Login source values."""

    PASSCODE = "PASSCODE"
    BCSC = "BCSC"
    BCEID = "BCEID"
    STAFF = "IDIR"
    BCROS = "BCROS"
    API_GW = "API_GW"
    IDIR = "IDIR"


class Role(Enum):
    """User Role."""

    VIEWER = "view"
    EDITOR = "edit"
    PUBLIC_USER = "public_user"
    ACCOUNT_HOLDER = "account_holder"
    GOV_ACCOUNT_USER = "gov_account_user"
    ANONYMOUS_USER = "anonymous_user"
    ACCOUNT_IDENTITY = "account_identity"
    MANAGE_EFT = "manage_eft"

    SYSTEM = "system"
    TESTER = "tester"

    STAFF = "staff"
    STAFF_VIEW_ACCOUNTS = "view_accounts"
    STAFF_MANAGE_ACCOUNTS = "manage_accounts"
    STAFF_SEARCH = "search"
    STAFF_CREATE_ACCOUNTS = "create_accounts"
    STAFF_MANAGE_BUSINESS = "manage_business"
    STAFF_SUSPEND_ACCOUNTS = "suspend_accounts"


class RegistrationStatus(Enum):
    """STRR Registration Status."""

    PENDING = "pending"
    APPROVED = "approved"
    MORE_INFO_NEEDED = "more info needed"
    DENIED = "denied"


class PropertyType(Enum):
    """STRR Property Type."""

    PRIMARY = "All or part of primary dwelling"
    SECONDARY = "Secondary suite"
    ACCESSORY = "Accessory dwelling unit"
    FLOAT_HOME = "Float home"
    OTHER = "Other"


class OwnershipType(Enum):
    """STRR Ownership Type."""

    OWN = "own"
    RENT = "rent"
    CO_OWN = "co-own"


class EventRecordType(Enum):
    """STRR Event Record Type."""

    SBC_ACCOUNT_CREATE = "create a new SBC account"
    SBC_ACCOUNT_ADDED_CONTACT = "added contact info to SBC account"
    INVOICE_GENERATED = "invoice generated for registration"
    INVOICE_PAYED = "invoice payed for registration"


class PaymentStatus(Enum):
    """Payment status codes."""

    CREATED = "CREATED"
    COMPLETED = "COMPLETED"
    PAID = "PAID"
    APPROVED = "APPROVED"
    DELETED = "DELETED"
    REFUNDED = "REFUNDED"
    FAILED = "FAILED"
