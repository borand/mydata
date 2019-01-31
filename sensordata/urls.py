from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'ping', views.ping),
    re_path(r'home/$', views.HomePageView.as_view(), name='sensordata_home'),

    ## SUBMIT DATA
    re_path(r'api/sub/(?P<datestamp>now)/sn/(?P<sn>.*)/val/(?P<val>.*)', views.api_submit_datavalue),    
    re_path(r'api/sub/(?P<datestamp>\d{4}\-\d{1,2}\-\d{1,2}-\d{1,2}:\d{1,2}:\d{1,2}\.*\d{0,6})/sn/(?P<sn>.*)/val/(?P<val>.*)$', \
                            views.api_submit_datavalue),

    # re_path(r'api/data/sn/(?P<serial_number>[a-zA-Z0-9-_\.]+)/(?P<today>today)/$', views.DataValueForDevDetail.as_view()),  
    re_path(r'api/data/sn/(?P<serial_number>[a-zA-Z0-9-_\.]+)/(?P<today>today)/', views.api_get_datavalue,  name='api_get_datavalue'),  
]