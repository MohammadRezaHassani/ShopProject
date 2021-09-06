from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from client.models import BaseClient

User = get_user_model()


# User Forms

class CustomUserCreationForm(forms.ModelForm):
    init_password = forms.CharField(label='password')
    confirm_password = forms.CharField(label='confirmation password')

    class Meta:
        model = User
        exclude = ()

    # TODO : password one clean password should be implemented

    def clean_confirm_password(self):
        pass1 = self.cleaned_data.get('init_password')
        pass2 = self.cleaned_data.get('confirm_password')
        if pass2 and pass1 and pass1 != pass2:
            raise ValidationError('password match Error')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('init_password'))
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        exclude = ()


# Login Forms

class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',

    }), label='Phone')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        password = cleaned_data.get('password')
        user = authenticate(phone=phone, password=password)
        if not user:
            raise forms.ValidationError('user Does Not exist')
        return cleaned_data


# Register Form

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = BaseClient
        fields = ['first_name', 'last_name', 'phone', 'email', 'password', 'confirm_password', 'image']
        widgets = {
            'password': forms.PasswordInput
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if User.objects.filter(phone=phone).exists():
            raise ValidationError('the same user with the same phone number')
        return phone

    def save(self, commit=True):
        client = super().save(commit=False)
        client.set_password(self.cleaned_data.get('password'))
        if commit:
            client.save()
        return client
