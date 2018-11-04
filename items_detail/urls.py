from django.conf.urls import url
from .views import Index, ManSingle, Mens, MensSingle, Womens, MensAccessory, WomensAccessory, MensTop, MensLegs

urlpatterns = [
    url(r'^index/', Index.as_view(), name='shopping_index'),
    url(r'^man_single/(?P<pk>\d+)/$', ManSingle.as_view(), name='man_single'),
    url(r'^mens/', Mens.as_view(), name='mens'),
    url(r'^mansingle/(?P<pk>\d+)/$', MensSingle.as_view(), name='menssingle'),
    url(r'^womens/', Womens.as_view(), name='womens'),
    # url(r'^womansingle/(?P<pk>\d+)/$', WomensSingle.as_view(), name='womansingle'),
    url(r'^mensaccessory/', MensAccessory.as_view(), name='mensaccessory'),
    url(r'^womensaccessory/', WomensAccessory.as_view(), name='womensaccessory'),
    url(r'^menstop/', MensTop.as_view(), name='menstop'),
    url(r'^menslegs/', MensLegs.as_view(), name='menslegs'),



]
