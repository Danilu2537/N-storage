from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

from storages.models import Storage
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
    serializer_class = StorageSerializer


# Вью классы единиц техники
class TechnicCreateView(CreateAPIView):
    serializer_class = TechnicSerializer


class TechnicListView(ListAPIView):
    serializer_class = TechnicSerializer


class TechnicView(RetrieveUpdateDestroyAPIView):
    serializer_class = TechnicSerializer


# Вью классы сотрудников
class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer


class EmployeeListView(ListAPIView):
    serializer_class = EmployeeSerializer


class EmployeeView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
