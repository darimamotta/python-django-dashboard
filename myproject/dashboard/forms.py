from django import forms
from .models import Product
from .models import Order
from .models import Result


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity']

class ResultForm(forms.ModelForm):
    result = forms.CharField()
    class Meta:
        model = Result
        fields = ['id', 'a', 'b', 'res']
