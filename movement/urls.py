from django.urls import path

from movement.views import (
    DispatchCreate,
    DispatchList,
    ReceiptCreate,
    ReceiptList,
    UnitsList,
)

app_name = 'movement'

urlpatterns = [
    # Эндпоинт количества единиц техники
    path('units/', UnitsList.as_view(), name='list-units'),
    # Эндпоинты отпусков
    path('dispatch/', DispatchList.as_view(), name='list-dispatch'),
    path('dispatch/create/', DispatchCreate.as_view(), name='create-dispatch'),
    # Эндпоинты приходов
    path('receipt/create/', ReceiptCreate.as_view(), name='create-receipt'),
    path('receipt/', ReceiptList.as_view(), name='list-receipt'),
]
