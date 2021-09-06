from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseClient(User):
    credit = models.IntegerField(blank=True, null=True)




# Create your models here.
