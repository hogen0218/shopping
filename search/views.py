from django.shortcuts import render,redirect
from items_detail.models import Item
from django.db.models import Q
from .filter import ProductFilter
from django.views.generic import TemplateView
# Create your views here.


def product_list(request):
    f = ProductFilter(request.GET, queryset=Item.objects.all())
    return render(request, 'bootstrap/searchlist.html', {'filter': f})


class S(TemplateView):
    template_name = "bootstrap/searchlist.html"

    def get_context_data(self, **kwargs):

        objects = ProductFilter(self.request.GET, queryset=Item.objects.all())
        kwargs['filter']= objects
        return super().get_context_data(**kwargs)