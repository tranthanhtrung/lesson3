from django.shortcuts import render
from rest_framework import serializers, viewsets

from . import models


class CatergoriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.categories
		fields = '__all__'

class CRUD_categories(viewsets.ModelViewSet):
	queryset = models.categories.objects.all()
	serializer_class = CatergoriesSerializer

class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Products
		fields = '__all__'
		depth = 2

class CRUD_products(viewsets.ModelViewSet):
	queryset = models.Products.objects.all()
	serializer_class = ProductsSerializer

class OrdersSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Products
		fields = '__all__'
		depth = 2

class CRUD_orders(viewsets.ModelViewSet):
	queryset = models.orders.objects.all()
	serializer_class = OrdersSerializer