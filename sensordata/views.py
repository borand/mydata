

# Create your views here.
import datetime
import logging
import json
import time

from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.views.generic import View, ListView, DetailView
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from .data_utils import data_value_submission

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from . import models
from .serializers import UserSerializer, GroupSerializer, UnitsSerializer


logger = logging.getLogger('app')

#########################################################################
#
# Group of Home views
#

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def ping(request):
    msg = "pong %s" % (datetime.datetime.now())
    logger.debug(msg)
    return HttpResponse(msg)


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        msg = "Sensordata app loaded @ %s" % (datetime.datetime.now())
        context = super(HomePageView, self).get_context_data(**kwargs)
        # context['device_instance'] = models.DeviceInstance.objects..filter(private=False).order_by('device')
        context['msg'] = msg
        logger.info(msg)
        return context


class GatewayMonView(TemplateView):
    template_name = "gateway_console.html"

    def get_context_data(self, **kwargs):
        msg = "GatewayMonView app loaded"
        context = super(GatewayMonView, self).get_context_data(**kwargs)
        context['msg_2'] = msg
        return context


########################################################################
#
# Basic object display classes
#


def api_submit_datavalue(request, datestamp, sn, val):
    msg = "[SUBMITTED] datestamp: %s, sn: %s, val: %s" % (datestamp, sn, val)
    logger.info(msg)
    try:
        results = data_value_submission(datestamp, sn, val, request.META.get('REMOTE_ADDR'))
    except Exception as E:
        results = ' Exception: {0}'.format(E)
    return HttpResponse(json.dumps({"msg": msg, "response": results}))


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

# class UnitsViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = models.Units.objects.all()
#     serializer_class = UnitsSerializer



# class DataValueDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
#     queryset = models.DataValue.objects.all()
#     serializer_class = DataValueSerializer
#     filter_fields = ('device_instance__serial_number')


# class DataValueForDevDetail(generics.ListAPIView):
#     # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
#     serializer_class = DataValuePairSerializer

#     def get_queryset(self, **kwargs):

#         logger.debug('get_queryset(kwargs= %s)' % str(self.kwargs))
#         to = time.time()
#         serial_number = self.kwargs['serial_number']
#         queryset = models.DataValue.objects.filter(device_instance__serial_number=serial_number).order_by(
#             'data_timestamp__measurement_timestamp')
#         logger.debug("Query time             = %.3f" % (time.time() - to))

#         if 'today' in self.kwargs:
#             logger.debug("Filtering: todays data")
#             queryset = queryset.filter(data_timestamp__measurement_timestamp__gte=datetime.date.today())

#             # From web
#             # today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
#             # today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
#             # queryset = queryset.filter(data_timestamp__measurement_timestamp__range=(today_min, today_max))

#         if 'from' in self.kwargs and 'to' in self.kwargs:
#             logger.debug("Filtering: from %s to %s" % (self.kwargs.has_key('from'), self.kwargs.has_key('to')))
#             start_date = datetime.datetime.strptime(self.kwargs['from'].split('.')[0], "%Y-%m-%d")
#             end_date = datetime.datetime.strptime(self.kwargs['to'].split('.')[0], "%Y-%m-%d")
#             queryset = queryset.filter(data_timestamp__measurement_timestamp__range=(start_date, end_date))

#         logger.debug("Returning dataset")
#         return queryset