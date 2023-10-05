from django.urls import path

from reports.views import hist, index, storages, technics

urlpatterns = [
    path('', index, name='index'),
    path('storages/', storages, name='склады'),
    path('technics/', technics, name='техника'),
    path('hist/', hist, name='гистограмма'),
]
