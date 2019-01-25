from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)
router.register(r'units', api_views.UnitsViewSet)
router.register(r'man', api_views.ManufacturerSerializer)
router.register(r'time', api_views.TimeStampSerializer)
router.register(r'signal', api_views.PhysicalSignalSerializer)
router.register(r'dev', api_views.DeviceSerializer)
router.register(r'gateway', api_views.DeviceGatewaySerializer)
router.register(r'location', api_views.LocationSerializer)
router.register(r'deviceinstance', api_views.DeviceInstanceSerializer)
router.register(r'datavalue', api_views.DataValueSerializer)


urlpatterns = [
    re_path(r'^', include(router.urls)),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# urlpatterns = format_suffix_patterns(urlpatterns)