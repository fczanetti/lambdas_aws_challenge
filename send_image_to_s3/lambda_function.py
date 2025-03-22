import logging
import boto3
from datetime import datetime
import base64
import os


s3 = boto3.resource(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS"))
bucket_name = os.environ.get("AWS_BUCKET_NAME")
bucket = s3.Bucket(bucket_name)

log = logging.getLogger()
log.setLevel(logging.INFO)

def lambda_handler(event, context):
    log.info("Starting lambda to send image to S3.")
    
    image = event["body-json"]
    filename = event["params"]["querystring"]["filename"]
    decoded_image = base64.b64decode(image)

    try:
        bucket.put_object(Body=decoded_image, Key=f"images/{filename}")
    except Exception as e:
        log.info(f"An exception was raised when trying to send an image to S3: {e}")
