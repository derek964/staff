from django.conf.urls import url
from stumgr.views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^index/', index),
    url(r'^stuinfo/', stuinfo),
    url(r'^selcourse/', selcourse),
    url(r'^queryscore/', queryscore),
    url(r'^mopasswd/', mopasswd),
]
