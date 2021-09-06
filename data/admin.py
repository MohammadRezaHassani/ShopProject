from django.contrib import admin
from .models import *

admin.site.register(BaseComment)
admin.site.register(BaseScore)
admin.site.register(BaseProductScore)
admin.site.register(BaseProductComment)
# Register your models here.
