from django.shortcuts import render
from .models import Heading,Title,Downbase,Logistic

# Create your views here.
def index(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    # veggie = Veggie.objects.first()
    logistic = Logistic.objects.all()
    context={
        'address': getattr(heading,'address','' ),
        'email': getattr(heading,'email',''),
        'title': getattr(title,'title',''),
        'social_handle': getattr(downbase,'social_handle',''),
        # 'company_name': getattr(veggie,'company_name',''),
        # 'todo': getattr(veggie,'todo',''),
        # 'percent': getattr(veggie,'percent',''),
        "logistic": logistic,
    }
    return render(request,'pages/index.html',context)
def shop(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    context={
        'address': getattr(heading,'address','' ),
        'email': getattr(heading,'email',''),
        'title': getattr(title,'title',''),
        'social_handle': getattr(downbase,'social_handle','')
    }
    return render(request,'pages/shop.html',context)
def shop_detail(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    context={
        'address': getattr(heading,'address','' ),
        'email': getattr(heading,'email',''),
        'title': getattr(title,'title',''),
        'social_handle': getattr(downbase,'social_handle','')
    }
    return render(request,'pages/shop-detail.html',context)

def cart(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    context={
        'address': getattr(heading,'address','' ),
        'email': getattr(heading,'email',''),
        'title': getattr(title,'title',''),
        'social_handle': getattr(downbase,'social_handle','')
    }
    return render(request,'pages/cart.html', context)

def checkout(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    context={
        'address': getattr(heading,'address','' ),
        'email': getattr(heading,'email',''),
        'title': getattr(title,'title',''),
        'social_handle': getattr(downbase,'social_handle','')
    }
    return render(request,'pages/checkout.html', context)


def testimonial(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    context={
        'address': getattr(heading,'address','' ),
        'email': getattr(heading,'email',''),
        'title': getattr(title,'title',''),
        'social_handle': getattr(downbase,'social_handle','')
    }
    return render(request,'pages/testimonial.html', context)

def error(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    context={
        'address': getattr(heading,'address','' ),
        'email': getattr(heading,'email',''),
        'title': getattr(title,'title',''),
        'social_handle': getattr(downbase,'social_handle','')
    }
    return render(request, 'pages/404.html', context)

def contact(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    context={
        'address': getattr(heading,'address','' ),
        'email': getattr(heading,'email',''),
        'title': getattr(title,'title',''),
        'social_handle': getattr(downbase,'social_handle','')
    }
    return render(request, 'pages/contact.html', context)