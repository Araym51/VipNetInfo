from django.contrib import admin

from .models import VipNetInfo

# Register your models here.

@admin.register(VipNetInfo)
class VipNetInfoAdmin(admin.ModelAdmin):
    list_display = ('pc_name', 'operation_system','hdd_number', 'hdd_serial', 'inventory_number', 'pc_model',
                     'pc_mac_address', 'kaspersky', 'vipnet_name', 'office_number', 'username', 'first_name',
                     'last_name', 'fathers_name', 'division', 'position', 'created',)
    fields = ('__all__',)
    search_fields = ('username', 'vipnet_name')
    ordering = ('username',)
