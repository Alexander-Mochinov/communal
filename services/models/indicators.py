from django.db import models

class Counter(models.Model):

    class Parameter(models.TextChoices):
        INDICATORS_HOT_WATER = "INDICATORS_HOT_WATER", "Горячая вода"
        INDICATORS_COLD_WATER = "INDICATORS_COLD_WATER", "Холодная вода"
        INDICATORS_LIGHT_DAY = "INDICATORS_LIGHT_DAY", "Дневной период"
        INDICATORS_LIGHT_NIGHT = "INDICATORS_LIGHT_NIGHT", "Ночной период"

    name = models.CharField("Показатель", choices=Parameter.choices, max_length=100, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Indicators(models.Model):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    address = models.ForeignKey("users.Address", on_delete=models.CASCADE, null=True)
    counter = models.ForeignKey("services.Counter", on_delete=models.CASCADE, null=True)
    date_send = models.DateTimeField(verbose_name="Дата отправки", null=True, blank=True, auto_now_add=True)
    indicator = models.PositiveIntegerField(verbose_name="Показатель", default=0)

    def __str__(self) -> str:
        return f"{self.indicator}/{self.counter.get_name_display()}"