from django.contrib import admin

from movement.models import Dispatch, Receipt, Units


@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('storage', 'technic', 'count')
    search_fields = ('storage', 'technic')
    fieldsets = ((None, {'fields': ('storage', 'technic', 'count')}),)


@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    list_display = ('storage', 'technic', 'count')
    search_fields = ('storage', 'technic')
    fieldsets = ((None, {'fields': ('storage', 'technic', 'count', 'employee')}),)


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('storage', 'technic', 'count')
    search_fields = ('storage', 'technic')
    fieldsets = ((None, {'fields': ('storage', 'technic', 'count', 'employee')}),)
