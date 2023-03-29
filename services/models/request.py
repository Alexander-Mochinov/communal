import uuid

from django.db import models


class Request(models.Model):

    class StatusRequest(models.TextChoices):

        UNDER_CONSIDERATION = "На рассмотрении"
        PROCESSED = "Обработано"
        CLOSED = "Закрыта"

    number = models.UUIDField(default=uuid.uuid4)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    type_request = models.CharField(verbose_name="Тип заявки", max_length=100, null=True)
    status = models.CharField(verbose_name="Статус", choices=StatusRequest.choices, max_length=100, default=StatusRequest.PROCESSED.name)
    date_create = models.DateTimeField(verbose_name="Дата создания", null=True, blank=True, auto_now_add=True)
    answer = models.TextField(verbose_name="Ответ", null=True)
    appeal = models.TextField(verbose_name="Обращение")
