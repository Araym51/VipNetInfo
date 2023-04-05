from django.contrib import admin

from .models import VipNetInfo, Town, AdressInfo


# Register your models here.

@admin.register(VipNetInfo)
class VipNetInfoAdmin(admin.ModelAdmin):
    list_display = ('vipnet_name', 'address', 'pc_name', 'inventory_number', 'division', 'created',)
    fields = ('pc_name', 'operation_system', 'hdd_number', 'hdd_serial', 'inventory_number', 'pc_model',
              'pc_mac_address', 'kaspersky', 'vipnet_name', ('address', 'office_number',), ('username', 'first_name',),
              ('last_name', 'fathers_name',), ('division', 'position',), 'created',)
    search_fields = ('username', 'vipnet_name')
    ordering = ('username',)

@admin.register(Town)
class TownListAdmin(admin.ModelAdmin):
    list_display = ('town_name',)
    fields = ('town_name',)
    ordering = ('town_name',)


@admin.register(AdressInfo)
class AddressInfoAdmin(admin.ModelAdmin):
    list_display = ('town_name', 'address',)
    fields = ('town_name', 'address',)
    ordering = ('town_name',)
