from client.models import *
from core.models import BaseModel


class BaseAddress(BaseModel):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    longitude = models.IntegerField()
    latitude = models.IntegerField()


class ClientAddress(BaseAddress):
    client_id = models.OneToOneField(BaseClient, on_delete=models.RESTRICT)


# Create your models here.
