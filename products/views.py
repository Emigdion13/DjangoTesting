from django.shortcuts import render

from .forms import ProductForm,RawProductForm

# Create your views here.
from .models import Product


def product_create_view(request):

    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)# the ** turns  the arguments into a serializable object and pass it
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "products/product_create.html", context) 

#def product_create_view(request):

    #print(request)
    ##print(request.GET['title'])
    #print(request.GET)
    #print(request.POST)

    #title = request.POST.get('title')
    #print(title)
    ##Product.objects.create(title=my_new_title)
    ##form = ProductForm(request.POST or None)

    #context = { 
    #}
    #return render(request, "products/product_create.html", context)

#def product_create_view(request):

#    form = ProductForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = ProductForm()

#    context = { "form" :  form 
#    }
#    return render(request, "products/product_create.html", context)

def product_detail_view(request):

    print(request)
    print(request.POST)
    obj = Product.objects.get(id=1)
    #context = {
    #    'title': obj.title,
    #    'description': obj.description,
    #}

    context = { "object" :  obj 
    }
    return render(request, "products/product_details.html", context)