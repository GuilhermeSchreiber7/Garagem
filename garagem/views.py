from rest_framework.viewsets import ModelViewSet

from garagem.models import acessory,  color, category, brand,  model, vehicle, customer
from garagem.serializers import AccessorySerializer, ColorSerializer,  CategorySerializer, BrandSerializer, ModelSerializer, VehicleSerializer, CustomerSerializer, VehicleListSerializer, VehicleDetailSerializer

# Create your views here.

class AccessoryViewSet(ModelViewSet):
    queryset = acessory.objects.all()
    serializer_class = AccessorySerializer

class ColorViewSet(ModelViewSet):
    queryset = color.objects.all()
    serializer_class = ColorSerializer

class CategoryViewSet(ModelViewSet):
    queryset = category.objects.all()
    serializer_class = CategorySerializer

class BrandViewSet(ModelViewSet):
    queryset = brand.objects.all()
    serializer_class = BrandSerializer

class ModelViewSet(ModelViewSet):
    queryset = model.objects.all()
    serializer_class = ModelSerializer

class VehicleViewSet(ModelViewSet):
    queryset = vehicle.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return VehicleListSerializer  
        elif self.action == "retrieve":
            return VehicleDetailSerializer
        return VehicleSerializer 

class CustomerViewSet(ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = CustomerSerializer


