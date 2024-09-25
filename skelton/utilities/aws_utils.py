import logging
from typing import Any, Dict
from urllib.parse import urlparse

import boto3

logger = logging.getLogger(__name__)


def get_secret(secret_name: str, region_name: str = "us-east-1") -> dict:
    """
    Get a dictionary from AWS secrets manager
    Args:
        secret_name: Name of the AWS secret
        region_name: AWS region name
    Returns:
        Dictionary containing the secret values
    """
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    get_secret_value_response = client.get_secret_value(SecretId=secret_name)

    return eval(get_secret_value_response["SecretString"])


def read_from_s3(s3_path: str, **kwargs) -> bytes:
    """
    Read an s3 object and return the payload
    Args:
        s3_path: Path to s3 object
    Returns: Bytes of the s3 object
    """
    s3_url = S3Url(s3_path)
    s3_client = boto3.resource("s3", **kwargs)
    s3object = s3_client.Object(s3_url.bucket, s3_url.key)
    return s3object.get()["Body"]


def write_to_s3(s3_path, data: Any, *args, **kwargs):
    """Writes arbitrary data to an s3 path

    Args:
        s3_path: s3 desired filepath
        data: arbitrary data

    Returns:
        success of the object being added
    """
    aws_cred_keys = ["aws_access_key_id", "aws_secret_access_key", "aws_session_token"]
    aws_creds = {k: v for k, v in kwargs.items() if k in aws_cred_keys}
    kwargs = {k: v for k, v in kwargs.items() if k not in aws_cred_keys}

    url_obj = S3Url(s3_path)
    s3_client = boto3.resource("s3", **aws_creds)

    s3object = s3_client.Object(url_obj.bucket, url_obj.key)
    s3_args = kwargs.pop("s3_additional_kwargs", None)

    logger.info(f"Publishing to {url_obj} with these options {kwargs}")

    if s3_args:
        kwargs.update(s3_args)
    else:
        kwargs = {}

    return s3object.put(Body=data, *args, **kwargs)
