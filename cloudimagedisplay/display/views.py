from django.shortcuts import render
from django.http import HttpResponse
from boto.s3.connection import S3Connection

def index(request):
    conn = S3Connection('AKIAIMOTKO2QJIH4LOPA', 'M8AR4oVL/8hYS9bXqbWQ9alCot6UWfWHwFfTzXDZ')
    bucket = conn.get_bucket('arn:aws:s3:::to-do-list-cloud-images', validate=False)

    for key in bucket.list(prefix='dir-in-bucket'):
        print (key.name.encode('utf-8'))

    context = {'bucket': bucket}
    return render(request, "home.html", context)

def display_view(request, url):
    # image = request.GET.get('q', '')
    context = {'image_url': url}
    print(url)
    return render(request, "home.html", context)