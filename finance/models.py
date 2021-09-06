from client.models import *
from core.models import TimeStampMixin, BaseModel
from product.models import *

User = get_user_model()


class MonetaryUnit(BaseModel, TimeStampMixin):
    currency_name = models.CharField(max_length=20)
    dollar_currency_value = models.FloatField()

    def __str__(self):
        return self.currency_name


class BasePrice(BaseModel, TimeStampMixin):
    monetary_unit = models.ForeignKey(MonetaryUnit, on_delete=models.PROTECT)
    amount = models.PositiveIntegerField()


class ProductPrice(BasePrice):
    product_id = models.OneToOneField(BaseProduct, on_delete=models.DO_NOTHING)


class BaseDiscount(BaseModel, TimeStampMixin):
    choice = (
        ('v', 'value'),
        ('p', 'percent')
    )
    mode = models.CharField(choices=choice, max_length=4)
    amount = models.IntegerField()
    max_used_number = models.IntegerField()
    off_code = models.CharField(max_length=30)
    persons = models.ManyToManyField(User, through='PersonDiscount')


class BaseProductDiscount(BaseDiscount):
    product_id = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)


# define a many to many relationship here

class PersonDiscount(BaseModel):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.ForeignKey(BaseDiscount, on_delete=models.CASCADE)
    used_number = models.IntegerField(default=0)


class BaseOrder(BaseModel):
    order_code = models.CharField(max_length=50)
    order_date = models.DateTimeField()
    final_price = models.IntegerField()
    monetary_unit_id = models.ForeignKey(MonetaryUnit, on_delete=models.RESTRICT)
    client_id = models.ForeignKey(BaseClient, on_delete=models.DO_NOTHING)


class BaseOrderItem(BaseModel):
    order_code = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    price = models.IntegerField()
    monetary_unit_id = models.ForeignKey(MonetaryUnit, on_delete=models.RESTRICT)
    product_id = models.ForeignKey(BaseProduct, on_delete=models.DO_NOTHING)



# Create your models here.
