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
        


        

        

        


# class DataValueSerializer(serializers.ModelSerializer):
#     # device_instance = serializers.Field(source='device_instance')
#     class Meta:
#         model = DataValue
#         fields = '__all__'
#         # fields = ('data_timestamp', 'device_instance','value')

# class DataValuePairSerializer(serializers.ModelSerializer):
#     data_timestamp = serializers.Field(source='data_timestamp.measurement_timestamp')
#     # device_instance = serializers.Field(source='device_instance.serial_number')
#     # device = serializers.Field(source='device_instance.device')
#     value = serializers.Field(source='get_value_pair')
#     class Meta:
#         model = DataValue
#         # fields = ('data_timestamp','value')
#         fields = ('data_timestamp', 'value',)


# class DataValuePairSerializer2(serializers.Serializer):
    # """
    # Adaptation of tutorial example to Units.
    # based on http://django-rest-framework.org/tutorial/1-serialization.html
    # """

    # logger.debug("DataValuePairSerializer2")
    # data_timestamp = serializers.DateTimeField()
    # value          = serializers.FloatField()

    # @property
    # def data(self):
    #     to = time.time()
    #     logger.debug("Found %d items matching criteria " % self.object.count())
    #     values_list = self.object.values_list('data_timestamp__measurement_timestamp', 'value')
    #     v = self.object.values_list('value', flat=True)
    #     t = self.object.values_list('data_timestamp__measurement_timestamp', flat=True)
    #     logger.debug("Making the list        = %.3f" % (time.time() - to))

    #     logger.debug("Preparing array for json transmision")
    #     data = []
    #     for data_pt in values_list:
    #         data.append([time.mktime(data_pt[0].timetuple()), data_pt[1]])

    #     logger.debug("Making value pair list = %.3f" % (time.time() - to))
    #     return data