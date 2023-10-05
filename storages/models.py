from django.db import models


class Storage(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=100)
    contacts = models.TextField()
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name


class Technic(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техники'

    def __str__(self):
        return self.model
