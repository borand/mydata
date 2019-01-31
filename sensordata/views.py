

# Create your views here.
import datetime
import logging
import json
import time
from django.utils import timezone

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
from .serializers import UserSerializer, GroupSerializer, UnitsSerializer, DataValuePairSerializer


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

def api_get_datavalue(request, **kwargs):
    # msg = "[SUBMITTED] datestamp: %s, sn: %s, val: %s" % (datestamp, sn, val)
    # logger.info(kwargs)

    # results = data_value_submission(datestamp, sn, val, request.META.get('REMOTE_ADDR'))
    serial_number = kwargs['serial_number']
    # logger.info(serial_number)
    queryset = models.DataValue.objects.filter(device_instance__serial_number=serial_number).order_by('data_timestamp__measurement_timestamp_sec')
    data = []
    values_list = []
    
    if 'today' in kwargs:
        # logger.debug("Filtering: todays data")
        kwargs['today'] = datetime.date.today().timetuple();
        queryset = queryset.filter(data_timestamp__measurement_timestamp_sec__gte=time.mktime(datetime.date.today().timetuple()))
        values_list = queryset.values_list('data_timestamp__measurement_timestamp_sec', 'value')

    if 'from' in kwargs and 'to' in kwargs:
        logger.debug("Filtering: from %s to %s".format(kwargs.has_key('from'), kwargs.has_key('to')))
        start_date = datetime.datetime.strptime(kwargs['from'].split('.')[0], "%Y-%m-%d")
        end_date = datetime.datetime.strptime(kwargs['to'].split('.')[0], "%Y-%m-%d")
        queryset = queryset.filter(data_timestamp__measurement_timestamp__range=(start_date, end_date))
        values_list = queryset.values_list('data_timestamp__measurement_timestamp_sec', 'value')

    for data_pt in values_list:
        data.append([data_pt[0], data_pt[1]])

    kwargs['data'] = data
    return HttpResponse(json.dumps(kwargs))
