from django.db import models


class HomeOwnersAssociation(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=100)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    address_legal = models.CharField(verbose_name="Юр. адрес", max_length=255)
    phone = models.CharField(verbose_name="Телефоный адрес", max_length=13)
