from django.contrib import admin
from rest_framework import routers
from django.urls import path
from .views import FarmersApiClass, CropApiView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns = [
    path("getfarmers/", FarmersApiClass.as_view(), name="farmers"),
    path('farmer/delete/<int:pk>/', FarmersApiClass.as_view(), name="farmer_delete"),
    path('farmer/update/<int:pk>/', FarmersApiClass.as_view(), name="farmer_delete"),
    path('farmer/profile/<int:pk>/', FarmersApiClass.as_view(), name="farmer_delete"),
    path('crop/getCrops', CropApiView.as_view(), name="crop_all" )
]
