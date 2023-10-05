from rest_framework import serializers

from storages.models import Employee, Storage, Technic


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class TechnicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technic
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'
