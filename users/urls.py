from django.conf.urls import url
from .views import Register, Login, user_logout

urlpatterns = [
    url(r'^register/', Register.as_view(), name='user_register'),
    url(r'^login/', Login.as_view(), name='user_login'),
    url(r'^logout/', user_logout, name='user_logout'),
]
