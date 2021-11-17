from django.shortcuts import render

from rest_framework import viewsets
from .models import Orders
from .serializers import OrdersSerializer

class OrdersViewSet(viewsets.ModelViewSet):
  serializer_class = OrdersSerializer
  queryset = Orders.objects.all()

  