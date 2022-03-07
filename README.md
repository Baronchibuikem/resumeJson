## About this Project

A Json formatted resume Django API app with AWS S3 bucket configuration

## To run

    git clone https://github.com/Baronchibuikem/resumeJson
    cd resumeJson
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py collectstatic
    python manage.py runserver

## Create a .env file in the root project and add the following and fill with your own AWS details and S3 bucket name

    AWS_STORAGE_PUBLIC_BUCKET_NAME=""
    AWS_STORAGE_PRIVATE_BUCKET_NAME=""
    AWS_ACCESS_KEY_ID=""
    AWS_SECRET_ACCESS_KEY=""
    AWS_S3_REGION_NAME="us-east-1"
    AWS_S3_SIGNATURE_VERSION='s3v4'
