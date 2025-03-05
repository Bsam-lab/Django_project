from django.shortcuts import render
from .models import Heading,Title,Downbase

# Create your views here.
def index(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    context={
        'address': heading.address,
        'email': heading.email,
        'title': title.title,
        'social_handle': downbase.social_handle
    }
    return render(request,'pages/index.html',context)
def shop(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    context={
        'address': heading.address,
        'email': heading.email,
        'title': title.title,
        'social_handle': downbase.social_handle
    }
    return render(request,'pages/shop.html',context)