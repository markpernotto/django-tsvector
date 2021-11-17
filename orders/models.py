from django.db import models
import uuid

class Orders(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  address = models.TextField()
  name = models.TextField()
  product_id = models.ForeignKey('product.Product', on_delete=models.PROTECT)
  customer_id = models.ForeignKey('customer.Customer', on_delete=models.PROTECT)

