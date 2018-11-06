from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    """创建评论表单"""
    class Meta:
        model = Comments
        fields = ('content', 'item')



