from django.db import models
import uuid

class Customer(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.TextField()
  address = models.TextField()

  class Meta:
    app_label = 'customer'