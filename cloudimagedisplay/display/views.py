from django.shortcuts import render
from django.http import HttpResponse
from boto.s3.connection import S3Connection
import boto3

def index(request):

    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(bucket)

    # conn = S3Connection('AKIAIMOTKO2QJIH4LOPA', 'M8AR4oVL/8hYS9bXqbWQ9alCot6UWfWHwFfTzXDZ')
    # bucket = conn.get_bucket('arn:aws:s3:::to-do-list-cloud-images', validate=False)
    #
    # for key in bucket.list(prefix='dir-in-bucket'):
    #     print (key.name.encode('utf-8'))

    bucket = "oui"

    context = {'bucket': bucket}
    return render(request, "home.html", context)

def display_view(request, url):
    context = {'image_url': url}
    return render(request, "display.html", context)