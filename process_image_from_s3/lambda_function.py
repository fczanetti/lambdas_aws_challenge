import logging
import boto3
from datetime import datetime
import base64
import os
import json


# s3 = boto3.resource(
#     "s3",
#     aws_access_key_id=os.environ.get("AWS_ACCESS_ID"),
#     aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS"))
# bucket_name = os.environ.get("AWS_BUCKET_NAME")
# bucket = s3.Bucket(bucket_name)

log = logging.getLogger()
log.setLevel(logging.INFO)

def lambda_handler(event, context):
    log.info("Starting lambda to process image from S3.")
    body = json.loads(event["Records"][0]["body"])
    key = body["Records"][0]["s3"]["object"]["key"]
    print(key)
