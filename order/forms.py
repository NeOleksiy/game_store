from django import forms
from order.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control", 'placeholder': 'Иван'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control", 'placeholder': 'Иванов'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control", 'placeholder': 'you@example.com'}))
    want_scamed = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        "class": "form-check-input"
    }))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'want_scamed')
