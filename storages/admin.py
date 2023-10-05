from django.contrib import admin

from storages.models import Employee, Storage, Technic


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ('title',)
    fieldsets = ((None, {'fields': ('title',)}),)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    fieldsets = ((None, {'fields': ('name', 'contacts', 'storage')}),)


@admin.register(Technic)
class TechnicAdmin(admin.ModelAdmin):
    list_display = ('model', 'id')
    search_fields = ('model',)
    fieldsets = ((None, {'fields': ('id', 'model', 'manufacturer', 'price')}),)
