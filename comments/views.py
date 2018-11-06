from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import FormView
from .forms import CommentForm
from .models import Comments
# Create your views here.



class CommentView(FormView):
    """判断评论成功与否"""
    form_class = CommentForm
    template_name = 'bootstrap/mens_single.html'

    def form_valid(self, form):
        user = self.request.user
        if not user:
            return HttpResponse('fail')
        Comments.objects.create(user=user, **form.cleaned_data)
        url = self.request.META['HTTP_REFERER']
        return redirect(url)

    def form_invalid(self, form):
        url = self.request.META['HTTP_REFERER']
        return redirect(url)