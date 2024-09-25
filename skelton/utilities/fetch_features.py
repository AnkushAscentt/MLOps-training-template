import os
import re

import boto3
import pandas as pd
import sagemaker
import yaml
from sagemaker.feature_store.feature_group import FeatureGroup
from sagemaker.feature_store.feature_store import FeatureStore
from sagemaker.session import Session

# env = os.getenv('ENVIRONMENT', default='dev')
with open(f"conf/tdspds-config.yml", "r") as file:
    config = yaml.safe_load(file)

role_arn = config["feature-store"]["arn"]
output_path = config["feature-store"]["fs-output-path"]
output_path_name = f"s3://{output_path}"


def fetch_features(feature_group_name):
    """
    Assumes a specified IAM role and retrieves features from a specified Amazon SageMaker Feature Group.

    This function assumes an IAM role using AWS Security Token Service (STS), initializes a SageMaker session
    with the assumed role's credentials, and then accesses a specific SageMaker Feature Group to retrieve its features.
    It returns the features in a pandas DataFrame.

    Parameters:
    - feature_group_name (str): The name of the SageMaker Feature Group from which to fetch the features.

    Returns:
    - pandas.DataFrame: A DataFrame containing the features from the specified Feature Group.

    Raises:
    - boto3.exceptions: If there is any issue with AWS service calls (like STS or SageMaker).
    - Exception: For any other issues encountered during the function execution.

    Example:
      feature_data = fetch_features('my-feature-group')
      print(feature_data.head())
    """

    sts_client = boto3.client("sts")
    role_to_assume_arn = role_arn
    role_session_name = "AssumedRoleInAccountA"
    role_session_name = re.sub("[^a-zA-Z0-9+=,.@-]", "", role_session_name)[:64]
    response = sts_client.assume_role(RoleArn=role_to_assume_arn, RoleSessionName=role_session_name)
    credentials = response["Credentials"]

    sagemaker_session = sagemaker.Session(
        boto_session=boto3.Session(
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
            region_name="us-east-1",
        )
    )

    feature_group = FeatureGroup(name=feature_group_name, sagemaker_session=sagemaker_session)
    feature_store = FeatureStore(sagemaker_session=sagemaker_session)

    result_df, query = feature_store.create_dataset(
        base=feature_group, output_path=output_path_name
    ).to_dataframe()

    return result_df
