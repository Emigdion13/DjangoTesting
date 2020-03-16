from django import forms


from .models import Product

#DjangoFOrms is the same as forms but the view will behave different this one seems to be the recomended
class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='Titulo', initial="", 
                    widget=forms.TextInput(attrs={"placeholder": "Your title"})) #required = false

    description = forms.CharField(required=False, 
                                widget=forms.Textarea(attrs={
                                    "placeholder": "My placeHolder",
                                    "class": "new-class-name two",
                                    "id" : "my-custom-id",
                                    "rows" : 20,
                                    'cols' : 120
                                }))
    price       = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title


#No textField  Normal Forms
class RawProductForm(forms.Form):
    #Widgets are the parameters that goes inside the form.Type(widgets)
    title       = forms.CharField(label='Titulo', initial="", widget=forms.TextInput(attrs={"placeholder": "Your title"})) #required = false
    description = forms.CharField(required=False, 
                                 widget=forms.Textarea(attrs={
                                     "placeholder": "My placeHolder",
                                     "class": "new-class-name two",
                                     "id" : "my-custom-id",
                                     "rows" : 20,
                                     'cols' : 120
                                 }))
    price       = forms.DecimalField(initial=199.99)