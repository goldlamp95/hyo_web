from .models import Family, Member, Image, Comment
from hyo.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3
from boto3.session import Session
from datetime import datetime
from django.contrib.auth.models  import User 

def upload_and_save(request, file_to_upload):
    session= Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME
        )
    s3 = session.resource('s3')

 
    now = datetime.now().strftime("%Y%H%M%S")
    img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
        Key = now+ file_to_upload.name,
        Body = file_to_upload
    )
    s3_url = 'https://hyohyobucket.s3.ap-northeast-2.amazonaws.com/'
    return {'s3_url':s3_url, 'now': now} 