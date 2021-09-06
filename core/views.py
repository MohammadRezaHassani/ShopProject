from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, CreateView

from .forms import *


class LoginFormView(FormView):
    template_name = 'authentication/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        user = authenticate(phone=self.request.POST['phone'], password=self.request.POST['password'])
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return redirect(reverse("core:my_login"))


# registration process is more difficult so we make it with function views


class RegisterView(CreateView):
    template_name = 'authentication/register.html'
    form_class = RegisterForm
    success_url = '/'


# just for testing

def main_view(request):
    return render(request, 'main.html', )

# Create your views here.
