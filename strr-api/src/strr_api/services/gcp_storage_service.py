# Copyright © 2024 Province of British Columbia
#
# Licensed under the BSD 3 Clause License, (the "License");
# you may not use this file except in compliance with the License.
# The template for the license can be found here
#    https://opensource.org/license/bsd-3-clause/
#
# Redistribution and use in source and binary forms,
# with or without modification, are permitted provided that the
# following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS”
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
"""Manages Auth service interactions."""
import uuid

from flask import current_app
from google.cloud import storage
from google.oauth2 import service_account


class GCPStorageService:
    """Service to save and load files from gcp buckets."""

    @classmethod
    def registration_documents_bucket(cls):
        """Get gcp bucket for saving or deleting registration documents."""

        # project_id = current_app.config.get("GCP_CS_PROJECT_ID")
        scope = current_app.config.get("GCP_CS_SA_SCOPE")
        bucket_id = current_app.config.get("GCP_CS_BUCKET_ID")
        # auth_key = current_app.config.get("GCP_AUTH_KEY")

        # TODO: fix service account setup
        service_account_info = {
            # 'type': 'service_account',
            # 'project_id': project_id,
            # 'private_key_id': GCP_SA_PRIVATE_KEY_ID,
            # 'private_key': str(GCP_SA_PRIVATE_KEY).replace('\\n', '\n'),
            # 'client_email': GCP_SA_CLIENT_EMAIL,
            # 'client_id': GCP_SA_CLIENT_ID,
            # 'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
            # 'token_uri': 'https://oauth2.googleapis.com/token',
            # 'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
            # 'client_x509_cert_url': GCP_SA_CERT_URL
        }
        credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=scope)
        storage_client = storage.Client(credentials=credentials)
        bucket = storage_client.bucket(bucket_id)
        return bucket

    @classmethod
    def upload_registration_document(cls, file_type, file_contents):
        """Save STRR uploaded document to gcp bucket."""

        registration_documents_bucket = cls.registration_documents_bucket()
        blob_name = str(uuid.uuid4())
        blob = registration_documents_bucket.blob(blob_name)
        blob.upload_from_string(data=file_contents, content_type=file_type)
        return blob_name

    @classmethod
    def delete_registration_document(cls, blob_name):
        """Delete registration document by id."""

        registration_documents_bucket = cls.registration_documents_bucket()
        blob = registration_documents_bucket.blob(blob_name)
        blob.delete()
