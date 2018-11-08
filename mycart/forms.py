from django import forms
from .models import LineItem



class AddForm(forms.ModelForm):
    class Meta:
        model = LineItem
        fields = ("item", "quantity")
