from rest_framework.serializers import ModelSerializer
from .models import Farmer, Crop


class FarmerSerializer(ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'


class CropSerializer(ModelSerializer):
    class Meta:
        model = Crop
        fields = "__all__"