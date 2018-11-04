from .models import User
from django import forms


class UserRegisterForm(forms.Form):
    # class Meta:
    #     model = User
    #     fields = ('username', 'password', 'email', 'phone_num')
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    phone_num = forms.CharField(max_length=50)


class UserLoginForm(forms.Form):
    # class Meta:
    #     model = User
    #     fields = ('username', 'password', 'email', 'phone_num')
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
