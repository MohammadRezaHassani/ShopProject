from django.urls import path
from .views import *


app_name = 'product'
urlpatterns = [
    path('', ProductListView.as_view(), name='main_page'),
    path('product_page/<slug:product_name>', ProductDetailPage.as_view(),name='product_page')

]