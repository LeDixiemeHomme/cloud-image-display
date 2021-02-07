from django.shortcuts import render
from django.http import HttpResponse
from boto.s3.connection import S3Connection
import boto3

def index(request):

    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')

    # allBuckets = s3.list_buckets()
    allObjectsFromABucket = s3.list_objects(Bucket='to-do-list-cloud-images')

    # print('Existing objects:')
    # for bucket in response['Contents']:
    #     print(bucket)
    # print('theBucket')
    # print(theBucket)
    # print("=============")

    # Output the bucket names
    # print('Existing buckets:')
    # for bucket in response['Buckets']:
    #     bucket = conn.get_bucket('bucket.Name', validate=False)

    context = {'bucket': allObjectsFromABucket['Contents']}
    return render(request, "home.html", context)

def display_view(request, url):
    context = {'image_url': url}
    return render(request, "display.html", context)