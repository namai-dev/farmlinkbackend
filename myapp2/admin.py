from django.contrib import admin
from .models import Farmer, Crop


# Register your models here.
admin.site.register(Farmer)
admin.site.register(Crop)