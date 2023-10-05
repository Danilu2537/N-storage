from django.urls import path

from storages.views import (
    EmployeeCreateView,
    EmployeeListView,
    EmployeeView,
    StorageCreateView,
    StorageListView,
    StorageView,
    TechnicCreateView,
    TechnicListView,
    TechnicView,
)

app_name = 'storages'

urlpatterns = [
    # Эндпоинты для работы со складами
    path('storage/create/', StorageCreateView.as_view(), name='create-storage'),
    path('storage/', StorageListView.as_view(), name='list-storage'),
    path('storage/<int:pk>/', StorageView.as_view(), name='view-storage'),
    # Эндпоинты для работы с единицами техники
    path('technic/create/', TechnicCreateView.as_view(), name='create-technic'),
    path('technic/', TechnicListView.as_view(), name='list-technic'),
    path('technic/<int:pk>/', TechnicView.as_view(), name='view-technic'),
    # Эндпоинты для работы с сотрудниками
    path('employee/create/', EmployeeCreateView.as_view(), name='create-employee'),
    path('employee/', EmployeeListView.as_view(), name='list-employee'),
    path('employee/<int:pk>/', EmployeeView.as_view(), name='view-employee'),
]
