from django.urls import path, include, re_path
from django.conf.urls import url
from .views import (
    StatusAPIView,
    #StatusCreateAPIView,
    #StatusDetailAPIView,
    #StatusUpdateAPIView,
    #StatusDeleteAPIView
    )

urlpatterns = [
    path('', StatusAPIView.as_view()),
    #path('create/', StatusCreateAPIView.as_view()),
    #re_path(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),
    #re_path(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    #re_path(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),
]
