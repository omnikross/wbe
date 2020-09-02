from . import views
from django.conf.urls import url
from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
     url(r'^sign-up/$', RegistrationAPIView.as_view()),
     url(r'^sign-in/$', LoginAPIView.as_view(), name='user_login'),
]