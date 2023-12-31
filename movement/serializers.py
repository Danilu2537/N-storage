from django.db import transaction
from rest_framework import serializers

from movement.models import Dispatch, Receipt, Units
from storages.models import Employee


class UnitsListSerializer(serializers.ModelSerializer):
    technic = serializers.StringRelatedField()
    storage = serializers.StringRelatedField()

    class Meta:
        model = Units
        exclude = ('id',)


class DispatchListSerializer(serializers.ModelSerializer):
    technic = serializers.StringRelatedField()
    storage = serializers.StringRelatedField()

    class Meta:
        model = Dispatch
        fields = '__all__'


class DispatchSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Dispatch:
        with transaction.atomic():
            validated_data['employee'] = Employee.objects.get(
                storage=validated_data['storage']
            )  # Сотрудник привязан к складу
            units = Units.objects.get(
                technic=validated_data['technic'], storage=validated_data['storage']
            )  # Получаем количество единиц техники
            if not units or units.count < validated_data['count']:
                raise ValueError(
                    'Такое количество единиц техники и склада не существует'
                )  # Если нет количества единиц техники или склада
            units.count -= validated_data['count']
            dispatch = super().create(validated_data)
            units.save()
        return dispatch

    class Meta:
        model = Dispatch
        exclude = ('employee',)


class ReceiptListSerializer(serializers.ModelSerializer):
    technic = serializers.StringRelatedField()
    storage = serializers.StringRelatedField()

    class Meta:
        model = Receipt
        fields = '__all__'


class ReceiptSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Receipt:
        with transaction.atomic():
            validated_data['employee'] = Employee.objects.get(
                storage=validated_data['storage']
            )  # Сотрудник привязан к складу
            units = Units.objects.get_or_create(
                technic=validated_data['technic'], storage=validated_data['storage']
            )[
                0
            ]  # Проверяем количество единиц техники, если нет - создаем
            units.count += validated_data['count']
            receipt = super().create(validated_data)
            units.save()
        return receipt

    class Meta:
        model = Receipt
        exclude = ('employee',)
