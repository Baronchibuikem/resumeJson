from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    location = settings.AWS_STORAGE_LOCATION_NAME
    bucket_name = settings.AWS_STORAGE_PUBLIC_BUCKET_NAME
    file_overwrite = False
    querystring_auth = False


class PrivateMediaStorage(S3Boto3Storage):  # noqa
    location = settings.AWS_STORAGE_LOCATION_NAME
    bucket_name = settings.AWS_STORAGE_PRIVATE_BUCKET_NAME
    default_acl = "private"
    file_overwrite = False
    custom_domain = False
