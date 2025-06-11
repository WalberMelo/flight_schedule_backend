import boto3
from botocore.exceptions import ClientError
import json

def get_secrets():
    secret_name = "prod/iag"
    region_name = "eu-south-2"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret_string = get_secret_value_response['SecretString']
    secret_dict = json.loads(secret_string)
 
    openai_key = secret_dict["OPENAI_API_KEY"]
    aviationstack_key = secret_dict["AVIATIONSTACK_KEY"]
    return openai_key, aviationstack_key