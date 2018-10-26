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
