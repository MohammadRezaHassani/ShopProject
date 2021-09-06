from core.models import *


class BaseCategory(BaseModel):
    name = models.CharField(max_length=30)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.name


def upload_to_path(instance, filename):
    return f"products/category_{instance.category_id.name}/{instance.name}.png"


class BaseProduct(BaseModel, TimeStampMixin):
    name = models.CharField(max_length=100)
    store_number = models.IntegerField()
    category_id = models.ForeignKey(BaseCategory, on_delete=models.RESTRICT)
    image = models.FileField(upload_to=upload_to_path, blank=True, null=True)

    def __str__(self):
        return self.name  # returns the name of the product


class BaseProperty(BaseModel, TimeStampMixin):
    color = models.CharField(max_length=10)
    product_id = models.ForeignKey(BaseProduct, on_delete=models.CASCADE)

    def get_fields(self):
        time_stamp_list = [(field.name, field.value_to_string(self))
                           for field in TimeStampMixin._meta.fields]
        property_list = [(field.name, field.value_to_string(self))
                         for field in BaseProperty._meta.fields]
        ans = list(set(property_list) - set(time_stamp_list))
        ans = [i for i in ans if not 'id' in i[0] or 'id' in i[1]]
        return ans

# Create your models here.
