from django.db import models


class Address(models.Model):

    town = models.CharField(verbose_name="Город", max_length=100, null=True, blank=True)
    street = models.CharField(verbose_name="Улица", max_length=100, null=True, blank=True)
    house = models.CharField(verbose_name="Дом", max_length=100, null=True, blank=True)
    frame = models.CharField(verbose_name="Корпус", max_length=100, null=True, blank=True)
    apartment = models.CharField(verbose_name="Квартира", max_length=100, null=True, blank=True)
