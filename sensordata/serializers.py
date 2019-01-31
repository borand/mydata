import time
import logging
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework import generics

from .models import Units, Location, Manufacturer, TimeStamp, DataValue,\
                    DeviceInstance, PhysicalSignal, Device, DeviceGateway

logger = logging.getLogger('app')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

# Sensordata

class UnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class TimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStamp
        fields = '__all__'

class PhysicalSignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalSignal
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceGatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceGateway
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class DeviceInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInstance
        fields = '__all__'

class DataValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataValue
        fields = ('data_timestamp', 'device_instance', 'value')

class DataValuePairSerializer(serializers.ModelSerializer):
    # data_timestamp = serializers.Field(source='data_timestamp.measurement_timestamp')
    # measurement_timestamp_sec = serializers.PositiveIntegerField(source='data_timestamp.measurement_timestamp_sec', read_only=True)
    # device_instance = serializers.Field(source='device_instance.serial_number')
    # device = serializers.Field(source='device_instance.device')
    value = serializers.FloatField()
    data_timestamp__measurement_timestamp_sec = serializers.FloatField()
    class Meta:
        model = DataValue
        fields = ('data_timestamp__measurement_timestamp_sec','value',)