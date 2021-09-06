from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager, PermissionsMixin
)
from django.db import models

from .validators import phone_validator, email_validator


# in the name of Allah

class BaseModel(models.Model):
    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    class Meta:
        abstract = True

    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    deletion_time = models.DateTimeField(default=None, null=True, blank=True)


def upload_to_path(instance, filename):
    return f"users/client/{instance.phone}.png"


class UserManager(BaseUserManager):
    def create_user(self, phone, password, first_name, last_name, **extra_fields):
        if not phone or first_name or last_name:
            raise ValueError('required fields missed')

        user = self.model(phone=phone, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, first_name, last_name, **extra_fields):
        if not phone or not first_name or not last_name:
            raise ValueError('required fields missed')

        user = self.model(phone=phone, password=password, first_name=first_name, last_name=last_name, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=10, validators=[phone_validator], unique=True)
    email = models.EmailField(max_length=200, blank=True, null=True,
                              verbose_name="Email Address",
                              validators=[email_validator])
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)

    # panel admin required fields
    is_staff = models.BooleanField(default=False, null=True, blank=True)
    is_superuser = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    join_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.FileField(upload_to=upload_to_path, default='static/user/anynomususer.jpg')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # setting the manager for our user model
    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
