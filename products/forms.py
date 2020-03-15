from django import forms


from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

#No textField
class RawProductForm(forms.Form):
    title       = forms.CharField(required=True) #required = false
    description = forms.CharField()
    price       = forms.DecimalField()