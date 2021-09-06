from django.urls import path

from .views import *

app_name = 'core'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='my_login'),
    path('register/', RegisterView.as_view(), name='my_register'),

]
