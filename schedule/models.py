from django.contrib.auth.models import User
from django.db import models


class TypeOfCut(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    value = models.FloatField()

    def __str__(self) -> str:
        return self.type


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.DateField()
    hour = models.TimeField()
    type_of_cut = models.ForeignKey(
        TypeOfCut,
        on_delete=models.PROTECT,
    )  # Noqa
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"Agendado {self.day}"
