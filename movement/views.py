from rest_framework.generics import CreateAPIView, ListAPIView

from movement.models import Dispatch, Receipt, Units
from movement.serializers import (
    DispatchListSerializer,
    DispatchSerializer,
    ReceiptListSerializer,
    ReceiptSerializer,
    UnitsListSerializer,
)


class UnitsList(ListAPIView):
    queryset = (
        Units.objects.all().prefetch_related('technic').prefetch_related('storage')
    )
    serializer_class = UnitsListSerializer


class DispatchList(ListAPIView):
    queryset = (
        Dispatch.objects.all().prefetch_related('technic').prefetch_related('storage')
    )
    serializer_class = DispatchListSerializer


class DispatchCreate(CreateAPIView):
    serializer_class = DispatchSerializer


class ReceiptList(ListAPIView):
    queryset = (
        Receipt.objects.all().prefetch_related('technic').prefetch_related('storage')
    )
    serializer_class = ReceiptListSerializer


class ReceiptCreate(CreateAPIView):
    serializer_class = ReceiptSerializer
