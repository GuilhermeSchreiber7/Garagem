from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from garagem.models import  acessory,  color, category, brand,  model, vehicle, customer

class AccessorySerializer(ModelSerializer):
    class Meta:
        model = acessory
        fields = '__all__'
        read_only_fields = ['id']


class ColorSerializer(ModelSerializer):
    class Meta:
        model = color
        fields = '__all__'
        read_only_fields = ['id']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'
        read_only_fields = ['id']

class BrandSerializer(ModelSerializer):
    class Meta:
        model = brand
        fields = '__all__'
        read_only_fields = ['id']

class ModelSerializer(ModelSerializer):
    class Meta:
        model = model
        fields = '__all__'
        read_only_fields = ['id']

class VehicleSerializer(ModelSerializer):
    class Meta:
        model = vehicle
        fields = '__all__'
        read_only_fields = ['id']

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'
        read_only_fields = ['id']
