from django.contrib import admin

from .models import *


@admin.register(MonetaryUnit, BasePrice, ProductPrice, BaseDiscount,
                BaseProductDiscount,  PersonDiscount,  BaseOrder, BaseOrderItem)
class FinanceAdmin(admin.ModelAdmin):
    pass
# Register your models here.
