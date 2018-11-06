from .models import User
from django import forms


class UserRegisterForm(forms.Form):
    """创建注册表单"""
    # class Meta:
    #     model = User
    #     fields = ('username', 'password', 'email', 'phone_num')
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    email = forms.CharField(max_length=50)
    phone_num = forms.CharField(max_length=50)


class UserLoginForm(forms.Form):
    """创建登录表单"""
    # class Meta:
    #     model = User
    #     fields = ('username', 'password', 'email', 'phone_num')
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
