from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, get_list_or_404
from .models import LineItem
from django.views.generic import FormView, TemplateView, DeleteView, UpdateView
from .forms import AddForm, DelForm


# Create your views here.



class Add(FormView):
    """加入购物车"""
    form_class = AddForm
    template_name = 'bootstrap/mens_single.html'

    def form_valid(self, form):
        user = self.request.user
        if not user:
            return HttpResponse('fail')
        data = form.cleaned_data
        id = data["item"].pk
        try:
            good = get_object_or_404(LineItem, user=user, item_id=id)
            good.quantity += 1
            good.save()
            url = self.request.META['HTTP_REFERER']
            return redirect(url)
        except Exception:
            LineItem.objects.create(user=user, **data)
            url = self.request.META['HTTP_REFERER']
            return redirect(url)

    def form_invalid(self, form):
        url = self.request.META['HTTP_REFERER']
        return redirect(url)


class Del(FormView):
    """删除一件购物记录"""
    form_class =DelForm
    template_name = 'bootstrap/cart1.html'

    def form_valid(self, form):
        user = self.request.user
        if not user:
            return HttpResponse('fail')
        data = form.cleaned_data
        good = LineItem.objects.get(**data)
        good.quantity -= 1
        good.save()
        if good.quantity == 0:
            good.delete()
        url = self.request.META['HTTP_REFERER']
        return redirect(url)


class ClearList(FormView):
    """清空购物车"""
    form_class = DelForm
    template_name = 'bootstrap/cart1.html'
    def form_valid(self, form):
        user = self.request.user
        if not user:
            return HttpResponse('fail')
        LineItem.objects.filter(user=user).delete()
        url = self.request.META['HTTP_REFERER']
        return redirect(url)




class CartList(TemplateView):
    template_name = "bootstrap/cart1.html"
    def get_context_data(self, **kwargs):
        user = self.request.user
        if not user:
            return HttpResponse('fail')
        kwargs['items'] = LineItem.objects.filter(user_id=user.id)
        from django.db.models import Sum, F, FloatField
        total = LineItem.objects.filter(user=user).aggregate(total=Sum(F('quantity') * F('item__price'), output_field=FloatField()))['total']
        kwargs['total'] = total
        return super().get_context_data(**kwargs)

