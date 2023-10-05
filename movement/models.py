from django.db import models

from storages.models import Employee, Storage, Technic


class Units(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT)
    technic = models.ForeignKey(Technic, on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        models.UniqueConstraint(fields=['storage', 'technic'], name='unique_units')
        verbose_name = 'Количество единиц техники'
        verbose_name_plural = 'Количество единиц техники'


class Dispatch(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT)
    technic = models.ForeignKey(Technic, on_delete=models.PROTECT)
    count = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Отпуск'
        verbose_name_plural = 'Отпуски'


class Receipt(models.Model):
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT)
    technic = models.ForeignKey(Technic, on_delete=models.PROTECT)
    count = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Приход'
        verbose_name_plural = 'Приходы'
