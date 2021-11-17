from django.db import models
import uuid

class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.TextField()
  manufacturer = models.TextField()

  class Meta:
    app_label = 'product'