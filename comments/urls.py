from django.conf.urls import url
from .views import CommentView

urlpatterns = [
    url(r'^user_comment/', CommentView.as_view(), name='user_comment'),
]
