from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *

User = get_user_model()


class MyUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('first_name', 'last_name', 'phone')
    filter_horizontal = ()
    list_filter = ('first_name', 'phone', 'email')

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'phone', 'last_login', 'image')}),
    )

    add_fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'phone', 'init_password',
                           'confirm_password', 'is_superuser', 'is_staff', 'image')}),
    )

    ordering = ('phone',)


admin.site.register(User, MyUserAdmin)
# Register your models here.
