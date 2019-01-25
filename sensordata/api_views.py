

# Create your views here.
import logging
from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from . import models
from .serializers import UserSerializer, GroupSerializer, UnitsSerializer, ManufacturerSerializer, TimeStampSerializer,\
PhysicalSignalSerializer, DeviceSerializer, DeviceGatewaySerializer, LocationSerializer, DeviceInstanceSerializer, DataValueSerializer



logger = logging.getLogger('app')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UnitsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Units.objects.all()
    serializer_class = UnitsSerializer


class ManufacturerSerializer(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class TimeStampSerializer(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.TimeStamp.objects.all()
    serializer_class = TimeStampSerializer    

class PhysicalSignalSerializer(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.PhysicalSignal.objects.all()
    serializer_class = PhysicalSignalSerializer      

class DeviceSerializer(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceGatewaySerializer(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.DeviceGateway.objects.all()
    serializer_class = DeviceGatewaySerializer

class LocationSerializer(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Location.objects.all()
    serializer_class = LocationSerializer    

class DeviceInstanceSerializer(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.DeviceInstance.objects.all()
    serializer_class = DeviceInstanceSerializer

class DataValueSerializer(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.DataValue.objects.all()
    serializer_class = DataValueSerializer