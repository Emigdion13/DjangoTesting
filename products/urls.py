"""Artificiali URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import product_detail_view, product_create_view, render_initial_data, product_delete_view, product_list_view

app_name = 'productsApp'
urlpatterns = [
    path('p/<int:myID>/', product_detail_view, name='productDetailed'),
    path('create', product_create_view, name='ProductCreate'),
    
    path('initial', render_initial_data, name='ProductCreateInitial'),
    path('<int:myID>/delete', product_delete_view, name='product_delete'),
    path('', product_list_view, name='ProductList'),

    path('sense', product_list_view,  name='ProductSense'),
]
