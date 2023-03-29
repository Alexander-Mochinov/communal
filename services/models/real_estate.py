from django.db import models


class RealEstate(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=10)
