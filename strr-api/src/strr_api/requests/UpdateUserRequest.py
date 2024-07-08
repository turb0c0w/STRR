# pylint: disable=C0103
# pylint: disable=R0913
"""
UpdateUserRequest request payload objects.
"""


class UpdateUserRequest:
    """UpdateUserRequest payload object."""

    def __init__(self, acceptTermsAndConditions, termsVersion):
        self.acceptTermsAndConditions = acceptTermsAndConditions
        self.termsVersion = termsVersion
