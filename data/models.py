from django.contrib.auth import get_user_model

from core.models import BaseModel, TimeStampMixin
from product.models import *

User = get_user_model()


class BaseScore(BaseModel, TimeStampMixin):
    min_score = models.PositiveIntegerField()
    max_score = models.PositiveIntegerField()
    object_score = models.PositiveIntegerField()


class BaseProductScore(BaseScore, TimeStampMixin):
    product_id = models.ForeignKey(BaseProduct, on_delete=models.DO_NOTHING)


# user strategy is done with user soft delete

class BaseComment(BaseModel, TimeStampMixin):
    comment_text = models.CharField(max_length=1000)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)  # soft_delete


class BaseProductComment(BaseComment):
    product_id = models.OneToOneField(BaseProduct, on_delete=models.RESTRICT)  # soft delete


# Create your models here.
