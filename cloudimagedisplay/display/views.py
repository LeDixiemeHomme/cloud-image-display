from django.shortcuts import render
from django.http import HttpResponse
from boto.s3.connection import S3Connection
import boto3

def index(request):

    s3 = boto3.client('s3')
    allObjectsFromABucket = s3.list_objects(Bucket='to-do-list-cloud-images')
    context = {'bucket': allObjectsFromABucket['Contents']}

    return render(request, "home.html", context)

def display_view(request, url):
    context = {'image_url': url}
    return render(request, "display.html", context)