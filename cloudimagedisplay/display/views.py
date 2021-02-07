from django.shortcuts import render
from django.http import HttpResponse
from boto.s3.connection import S3Connection
import boto3

def index(request):

    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    print("response is")
    print(response)

    print("=======")
    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(bucket)

    context = {'bucket': response['Buckets']}
    return render(request, "home.html", context)

def display_view(request, url):
    context = {'image_url': url}
    return render(request, "display.html", context)