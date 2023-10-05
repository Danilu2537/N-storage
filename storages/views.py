from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from storages.models import Employee, Storage, Technic
from storages.serializers import (
    EmployeeSerializer,
    StorageSerializer,
    TechnicSerializer,
)

"""
Вью сделаны для последующего расширения
"""


# Вью классы склада
class StorageCreateView(CreateAPIView):
    serializer_class = StorageSerializer


class StorageListView(ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageView(RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


# Вью классы единиц техники
class TechnicCreateView(CreateAPIView):
    serializer_class = TechnicSerializer


class TechnicListView(ListAPIView):
    queryset = Technic.objects.all()
    serializer_class = TechnicSerializer


class TechnicView(RetrieveUpdateDestroyAPIView):
    queryset = Technic.objects.all()
    serializer_class = TechnicSerializer


# Вью классы сотрудников
class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
