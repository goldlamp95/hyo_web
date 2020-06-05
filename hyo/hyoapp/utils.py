from .models import Family, Member
from file_upload.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STROAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3
from boto3.session import Session
from datetime import datetime
from django.contrib.auth.decorators  import User 

def upload_and_save(request, file_to_upload):
    session= Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME
        )
    s3 = session.resource('s3')

    user_pk = str(request.user.pk)+'/'
    now = datetime.now().strftime("%Y%H%M%S")
    img_object = s3.Bucket(AWS_STROAGE_BUCKET_NAME).put_object(
        Key = now + user.pk,
        Body = file_to_upload
    )
    s3_url = 'https://hyohyobucket.s3.ap-northeast-2.amazonaws.com/'
    image = Image.objects.create(
        image = s3_url + user.pk+ now + file_to_upload.name
        content = request.POST['content']
        image_author = request.user
    )