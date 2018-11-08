from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from users.forms import UserRegisterForm, UserLoginForm
from .models import Item
from comments.forms import CommentForm
from comments.models import Comments
from mycart.forms import AddForm
from django.core.urlresolvers import reverse_lazy


# Create your views here.



class Index(TemplateView):
    """创建主页面"""
    template_name = 'bootstrap/index.html'
    user_register_form = UserRegisterForm()
    user_login_form = UserLoginForm()


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




# MAN---------------------------------------------

class Mens(TemplateView):
    """创建男士商品的商品列表"""
    template_name = 'bootstrap/mens.html'
    user_register_form = UserRegisterForm()
    user_login_form = UserLoginForm()

    def get_context_data(self, **kwargs):
        kwargs['user_register_form'] = self.user_register_form
        kwargs['user_login_form'] = self.user_login_form
        kwargs['items'] = Item.objects.all()
        kwargs['all_items'] = Item.objects.filter(gender__name='MAN')
        return super().get_context_data(**kwargs)


class MensSingle(DetailView):
    """MAN 的详情页面"""
    template_name = 'bootstrap/mens_single.html'
    model = Item
    context_object_name = 'single_detail'
    user_register_form = UserRegisterForm()
    user_login_form = UserLoginForm()

    def get_context_data(self, **kwargs):
        kwargs['add_form'] = AddForm()
        kwargs['user_register_form'] = self.user_register_form
        kwargs['user_login_form'] = self.user_login_form
        kwargs['comment_form'] = CommentForm()
        kwargs['user_comments'] =Comments.objects.filter(item__id=kwargs['object'].pk).order_by('-comment_time')
        return super().get_context_data(**kwargs)



# MAN TOP
class MensTop(TemplateView):
    """创建男士上衣"""
    template_name = 'bootstrap/men_top.html'

    def get_context_data(self, **kwargs):
        kwargs['man_tops'] = Item.objects.filter(gender__name='MAN').filter(type__name='TOP')
        return super().get_context_data(**kwargs)

# MAN LEGS
class MensLegs(TemplateView):
    """创建男士裤子"""
    template_name = 'bootstrap/men_legs.html'

    def get_context_data(self, **kwargs):
        kwargs['man_legs'] = Item.objects.filter(gender__name='MAN').filter(type__name='LEGS')
        return super().get_context_data(**kwargs)

# man的ACCESSORY
class MensAccessory(TemplateView):
    """创建男士饰品"""
    template_name = 'bootstrap/mens_accessories.html'

    def get_context_data(self, **kwargs):
        kwargs['man_accs'] = Item.objects.filter(gender__name='MAN').filter(type__name='ACCESSORY')
        return super().get_context_data(**kwargs)

# MEN featured
class MensNewArrivals(TemplateView):
    """创建男士新商品"""
    template_name = 'bootstrap/newarrivals.html'

    def get_context_data(self, **kwargs):
        kwargs['man_items'] = Item.objects.filter(gender__name='MAN').filter(featured__name='New Arrivals')
        return super().get_context_data(**kwargs)

# ------------------------------------------------------------------------------------------



# WOMAN

class Womens(TemplateView):
    """关于女士商品的列表"""
    template_name = 'bootstrap/womens.html'

    def get_context_data(self, **kwargs):
        kwargs['woman_items'] = Item.objects.filter(gender__name='WOMAN')
        return super().get_context_data(**kwargs)



# WOman的ACCESSORY
class WomenAccessory(TemplateView):
    """创建女士饰品"""
    template_name = 'bootstrap/womens_accessories.html'

    def get_context_data(self, **kwargs):
        kwargs['woman_accs'] = Item.objects.filter(gender__name='WOMAN').filter(type__name='ACCESSORY')
        return super().get_context_data(**kwargs)

class WomenTops(TemplateView):
    """创建女士上衣"""
    template_name = 'bootstrap/women_top.html'

    def get_context_data(self, **kwargs):
        kwargs['women_top'] = Item.objects.filter(gender__name='WOMAN').filter(type__name='TOP')
        return super().get_context_data(**kwargs)

class WomenLegs(TemplateView):
    """创建女士裤子"""
    template_name = 'bootstrap/women_legs.html'

    def get_context_data(self, **kwargs):
        kwargs['women_legs'] = Item.objects.filter(gender__name='WOMAN').filter(type__name='LEGS')
        return super().get_context_data(**kwargs)


# ------------------------------------------------------------------------------------------

# accessory
class Accessory(TemplateView):
    """创建所有饰品"""
    template_name = 'bootstrap/accessory.html'

    def get_context_data(self, **kwargs):
        kwargs['all_accessory'] = Item.objects.filter(type__name='ACCESSORY')
        return super().get_context_data(**kwargs)