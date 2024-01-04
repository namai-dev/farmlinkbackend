from django.db import models


class Farmer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    location = models.CharField(max_length=255)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Crop(models.Model):
    crop_name = models.CharField(max_length=255)
    crop_type = models.CharField(max_length=255)
    number_stages = models.CharField(max_length=255)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='crops')


    def __str__(self):
        return self.crop_name
