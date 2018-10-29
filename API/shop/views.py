from django.shortcuts import render
from rest_framework import serializers, viewsets

from . import models


class ProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Products
		fields = '__all__'

class CatergoriesSerializer(serializers.ModelSerializer):
	products = ProductsSerializer(many = True)
	class Meta:
		model = models.categories
		fields = '__all__'

class Order_itemsSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.order_items
		fields = "__all__"
		depth = 2

class OrdersSerializer(serializers.ModelSerializer):
	items = Order_itemsSerializer(many = True)
	class Meta:
		model = models.orders
		fields = '__all__'


class CRUD_categories(viewsets.ModelViewSet):
	queryset = models.categories.objects.all()
	serializer_class = CatergoriesSerializer

class CRUD_products(viewsets.ModelViewSet):
	#permission_classes = [IsAuthenticated]
	queryset = models.Products.objects.all()
	serializer_class = ProductsSerializer

class CRUD_orders(viewsets.ModelViewSet):
	queryset = models.orders.objects.all()
	serializer_class = OrdersSerializer