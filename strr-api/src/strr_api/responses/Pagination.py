"""
Pagination response objects.
"""
from typing import List, Any

from pydantic import BaseModel


class Pagination(BaseModel):
    """Pagination response object."""

    count: int
    results: List[Any]
