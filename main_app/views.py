from django.shortcuts import render,redirect
from .models import Heading,Title,Downbase,Logistic,Vegie,Testimony
from . forms import UserRegristrationForm,UserLoginForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def index(request):
    heading = Heading.objects.first()
    title = Title.objects.first()
    downbase = Downbase.objects.first()
    vegie = Vegie.objects.first()
    logistic = Logistic.objects.all()
    testimony = Testimony.objects.all()
    context={
        'address': getattr(heading,'address','' ),
        'email': getattr(heading,'email',''),
        'title': getattr(title,'title',''),
        'social_handle': getattr(downbase,'social_handle',''),
        'name': getattr(vegie,'name',''),
        'offer': getattr(vegie,'offer',''),
        'rate': getattr(vegie,'rate',''),
        "logistic": logistic,
        'testimony': testimony
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

def register(request):
    if request.method == 'POST':
        form =UserRegristrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegristrationForm()
        return render(request, 'registration/register.html', {'form': form})
    return render(request, 'registration/welcome.html')
    
def login(request):
    form = UserLoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username= form.cleaned_data.get('email')
            password= form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)


            if user is not None:
                login(request, user)
                messages.success(request, f'welcome {username}!')
                return redirect('land')
            else:
                messages.info("Account does not exist, please register")
        else:
            form= UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})