from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import UserRegisterForm, UserLoginForm
from django.core.urlresolvers import reverse_lazy
from .models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


class Register(FormView):
    """用户注册"""
    template_name = 'bootstrap/index.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('shopping_index')

    def form_valid(self, form):
        data = form.cleaned_data
        User.objects.create_user(**data)
        return super().form_valid(form)


class Login(FormView):
    """用户登录"""
    template_name = 'bootstrap/index.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('shopping_index')

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(**data)
        if user is not None:
            login(self.request, user)
            url = self.request.META['HTTP_REFERER']
            return redirect(url)
        else:
            return super().form_valid(form)

def user_logout(request):
    """用户退出"""
    logout(request)
    url = request.META['HTTP_REFERER']
    return redirect(url)



