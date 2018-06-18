import os
import hvac
import boto3
import datetime

client = hvac.Client(url=os.environ['VAULT_ADDR'], token=os.environ['VAULT_TOKEN'])

print(os.environ)
"""
vault secrets enable -path=my-app kv
vault write my-app/my-app password=123
"""

awsSecret = client.read('python-app/aws')

print(awsSecret)

s3client = boto3.resource(
    's3',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=awsSecret['data']['aws_acces_key_id'],
    aws_secret_access_key=awsSecret['data']['aws_secret_access_key']
)

for bucket in s3client.buckets.all():
    print(bucket.name)

data = open('test.txt', 'rb')

