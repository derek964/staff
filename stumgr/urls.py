from django.conf.urls import url
from stumgr.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^index/', index),
]
