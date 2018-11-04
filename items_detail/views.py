from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from users.forms import UserRegisterForm, UserLoginForm
from .models import Item
# Create your views here.



class Index(TemplateView):
    template_name = 'bootstrap/index.html'
    user_register_form = UserRegisterForm()
    user_login_form = UserLoginForm

    def get_context_data(self, **kwargs):
        kwargs['user_register_form'] = self.user_register_form
        kwargs['user_login_form'] = self.user_login_form
        kwargs['items'] = Item.objects.all()
        kwargs['man_items'] = Item.objects.filter(gender__name='MAN')
        kwargs['woman_items'] = Item.objects.filter(gender__name='WOMAN')
        kwargs['hotlist_items'] = Item.objects.filter(gender__name='HOTLIST')
        kwargs['accessory_items'] = Item.objects.filter(type__name='ACCESSORY')
        kwargs['top_items'] = Item.objects.filter(type__name='TOP')
        kwargs['legs_items'] = Item.objects.filter(type__name='LEGS')
        return super().get_context_data(**kwargs)



class ManSingle(DetailView):
    template_name = 'bootstrap/mens_single.html'
    model = Item
    context_object_name = 'single_detail'




# 关于mens.html 的9个商品
class Mens(TemplateView):
    template_name = 'bootstrap/mens.html'
    user_register_form = UserRegisterForm()
    user_login_form = UserLoginForm

    def get_context_data(self, **kwargs):
        kwargs['user_register_form'] = self.user_register_form
        kwargs['user_login_form'] = self.user_login_form
        kwargs['items'] = Item.objects.all()
        kwargs['man_items'] = Item.objects.filter(gender__name='MAN')
        return super().get_context_data(**kwargs)


class MensSingle(DetailView):
    template_name = 'bootstrap/mens_single.html'
    model = Item
    context_object_name = 'single_detail'

#关于womens。html的9个商品
class Womens(TemplateView):
    template_name = 'bootstrap/womens.html'


    def get_context_data(self, **kwargs):
        kwargs['woman_items'] = Item.objects.filter(gender__name='WOMAN')
        return super().get_context_data(**kwargs)




# man的ACCESSORY
class MensAccessory(TemplateView):
    template_name = 'bootstrap/mens_accessories.html'

    def get_context_data(self, **kwargs):
        kwargs['man_accs'] = Item.objects.filter(gender__name='MAN').filter(type__name='ACCESSORY')
        return super().get_context_data(**kwargs)
# WOman的ACCESSORY
class WomensAccessory(TemplateView):
    template_name = 'bootstrap/womens_accessories.html'

    def get_context_data(self, **kwargs):
        kwargs['woman_accs'] = Item.objects.filter(gender__name='MAN').filter(type__name='ACCESSORY')
        return super().get_context_data(**kwargs)

# MAN TOP
class MensTop(TemplateView):
    template_name = 'bootstrap/men_top.html'

    def get_context_data(self, **kwargs):
        kwargs['man_tops'] = Item.objects.filter(gender__name='MAN').filter(type__name='TOP')
        return super().get_context_data(**kwargs)

# MAN LEGS
class MensLegs(TemplateView):
    template_name = 'bootstrap/men_legs.html'

    def get_context_data(self, **kwargs):
        kwargs['man_legs'] = Item.objects.filter(gender__name='MAN').filter(type__name='LEGS')
        return super().get_context_data(**kwargs)