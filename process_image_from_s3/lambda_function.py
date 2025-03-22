import logging
import boto3
from datetime import datetime
import base64
import os
import json
from PIL import Image, ImageOps
from io import BytesIO


s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS")
)
bucket_name = os.environ.get("AWS_BUCKET_NAME")

log = logging.getLogger()
log.setLevel(logging.INFO)

def lambda_handler(event, context):
    log.info("Starting lambda to process image from S3.")
    body = json.loads(event["Records"][0]["body"])
    key = body["Records"][0]["s3"]["object"]["key"]

    image_file = s3_client.get_object(Bucket=bucket_name, Key=key)
    image_content = image_file["Body"].read()  # return the image in bytes
    image = BytesIO(image_content)  # creates an image file in memory

    size = (400, 400)

    filename = key.split("/")[-1]

    with Image.open(image) as im:
        im = ImageOps.contain(im, size)
        
        new_image = BytesIO()
        im.save(new_image, format="PNG")

        new_image.seek(0)

    s3_client.put_object(Body=new_image, Bucket=bucket_name, Key=f"resized/{filename}")
