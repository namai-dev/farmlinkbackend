from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FarmerSerializer, CropSerializer
from .models import Farmer, Crop
from  rest_framework.response import Response
from rest_framework import status
# Create your views here.




class FarmersApiClass(APIView):
    def get(self, request):
        farmers = Farmer.objects.all()
        farmers_serial = FarmerSerializer(farmers, many=True)
        return Response(farmers_serial.data)

    def post(self, request):
        data = FarmerSerializer(data=request.data)
        if data.is_valid():
            data.save()
            print("saved")
            return Response(data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk = pk)
        except Farmer.DoesNotExist as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        farmer.delete()

        return Response(status=status.HTTP_200_OK)


    def put(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = FarmerSerializer(farmer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, pk):
        try:
            farmer = Farmer.objects.get(pk=pk)
        except Farmer.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FarmerSerializer(farmer)
        return Response(serializer.data, status=status.HTTP_302_FOUND)


class CropApiView(APIView):
    def get(self, request):
        crops = Crop.objects.all()
        crops_serializer = CropSerializer(crops, many=True)
        return Response(crops_serializer.data, status=status.HTTP_200_OK)
