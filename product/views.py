from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.models import BaseProduct


class ProductListView(ListView):
    template_name = 'main.html'
    model = BaseProduct
    context_object_name = 'products'


class ProductDetailPage(DetailView):
    template_name = 'product/ProductDetail.html'
    model = BaseProduct
    slug_field = 'name'
    slug_url_kwarg = 'product_name'
    context_object_name = 'product'


# test the redirect with what we have


# Create your views here.
