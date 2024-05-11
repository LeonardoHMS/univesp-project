from django.contrib.auth.models import User
from django.db import models


class TypeOfCut(models.Model):
    id = models.AutoField(primary_key=True)
    type_cut = models.CharField(max_length=255)
    value = models.FloatField()

    def __str__(self) -> str:
        return f"{self.type_cut}"


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    date_hour = models.DateTimeField(null=True, unique=True)
    type_of_cut = models.ForeignKey(
        TypeOfCut,
        on_delete=models.PROTECT,
    )  # Noqa
    obs = models.TextField(max_length=255, null=True)
    conclude = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"Agendado {self.date_hour}"
