from django.contrib import admin

# Register your models here.
from .models import *


class DataValueAdmin(admin.ModelAdmin):
    list_display = ['data_timestamp', 'device_instance', 'value']
    list_filter = ('device_instance', 'device_instance__location', 'device_instance__serial_number')


class DeviceGatewayAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'port', 'active', 'protocol', 'process_pid']
    list_editable = ['active']
    list_filter = ('active', 'protocol',)


class DeviceInstanceAdmin(admin.ModelAdmin):
    list_display = ['device', 'serial_number', 'gateway', 'location', 'physical_signal', 'active', 'private',
                    'accept_from_gateway_only']
    list_editable = ['active', 'serial_number', 'private', 'location', 'accept_from_gateway_only']
    list_filter = ['user', 'active', 'device', 'gateway', 'location']


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_name', 'model_number', 'units', 'manufacturer', 'update_rate', 'max_range', 'min_range',
                    'actuator']
    list_editable = ['update_rate', 'max_range', 'min_range']
    list_filter = ['manufacturer', 'device_name', 'model_number', 'actuator']


class DataObjectAdmin(admin.ModelAdmin):
    list_display = ['data_timestamp', 'device_instance', 'value']

admin.site.register(Units)
admin.site.register(Manufacturer)
admin.site.register(TimeStamp)
admin.site.register(PhysicalSignal)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceGateway, DeviceGatewayAdmin)
admin.site.register(Location)
admin.site.register(DeviceInstance, DeviceInstanceAdmin)
admin.site.register(DataValue, DataValueAdmin)
admin.site.register(Experiment)
admin.site.register(Note)
admin.site.register(DataObject)
