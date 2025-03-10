from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User= get_user_model()


class UserRegristrationForm(UserCreationForm):
    username = forms.CharField(label='',max_length=150, widget=forms.TextInput(attrs={'placeholder':'Unique Username'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'block py-3 w-2/3','placeholder':'email'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'mb-2','placeholder':'Email'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': '', 'placeholder':'Password'}))