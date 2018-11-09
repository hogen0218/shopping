from django.conf.urls import url
from .views import product_list, S
urlpatterns = [

    url(r'^search/', S.as_view(), name='search'),
    url(r'^list$', product_list),

]