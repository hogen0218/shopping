from django.conf.urls import url
from .views import Index, ManSingle, Mens, MensSingle, Womens, MensAccessory, \
    WomenAccessory, MensTop, MensLegs,MensNewArrivals, WomenTops, WomenLegs, Accessory

urlpatterns = [
    url(r'^index/', Index.as_view(), name='shopping_index'),
    url(r'^man_single/(?P<pk>\d+)/$', ManSingle.as_view(), name='man_single'),
    url(r'^mens/', Mens.as_view(), name='mens'),
    url(r'^mansingle/(?P<pk>\d+)/$', MensSingle.as_view(), name='menssingle'),
    url(r'^womens/', Womens.as_view(), name='womens'),
    url(r'^mensaccessory/', MensAccessory.as_view(), name='mensaccessory'),
    url(r'^womensaccessory/', WomenAccessory.as_view(), name='womensaccessory'),
    url(r'^menstop/', MensTop.as_view(), name='menstop'),
    url(r'^menslegs/', MensLegs.as_view(), name='menslegs'),
    url(r'^newarrivals/', MensNewArrivals.as_view(), name='newarrivals'),
    url(r'^womentops/', WomenTops.as_view(), name='womentops'),
    url(r'^womenlegs/', WomenLegs.as_view(), name='womenlegs'),
    url(r'^allaccessory/', Accessory.as_view(), name='allaccessory'),




]
