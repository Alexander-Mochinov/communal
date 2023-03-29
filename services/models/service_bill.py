from django.db import models


class ServiceBill(models.Model):
    service = models.ForeignKey("services.HomeOwnersAssociation", on_delete=models.CASCADE)
    price = models.IntegerField(default=0)