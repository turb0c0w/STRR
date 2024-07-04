"""
Auto Approval response objects.
"""
from typing import List, Optional
from pydantic import BaseModel

class AutoApproval(BaseModel):
    """Auto approval response object."""
    renting: Optional[bool] = None
    service_provider: Optional[bool] = None
    pr_exempt: Optional[bool] = None
    address_match: Optional[bool] = None
    business_license_required: Optional[bool] = None
    business_license_required_not_provided: Optional[bool] = None
    business_license_required_provided: Optional[bool] = None
    business_license_not_required_not_provided: Optional[bool] = None
    title_check: Optional[bool] = None
    status_to_set: Optional[str] = None # temp