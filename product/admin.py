from django.contrib import admin

from finance.models import ProductPrice
from .models import *


class ProductInline(admin.StackedInline):
    model = BaseProduct


class PropertyInline(admin.StackedInline):
    model = BaseProperty
    max_num = 1


class PriceInline(admin.StackedInline):
    model = ProductPrice


@admin.register(BaseCategory)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


@admin.register(BaseProduct)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PropertyInline, PriceInline]


@admin.register(BaseProperty)
class PropertyAdmin(admin.ModelAdmin):
    pass

# Register your models here.
