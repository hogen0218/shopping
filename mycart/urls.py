
from django.conf.urls import url
from .views import Add, CartList, Del, ClearList

urlpatterns = [

    url(r'^additems/', Add.as_view(), name='additems'),
    url(r'^delitems/', Del.as_view(), name='delitems'),
    url(r'^cartlist', CartList.as_view(), name='cartlist'),
    url(r'^clearlist/', ClearList.as_view(), name='clearlist'),

]