from django.urls import path, include, re_path
from django.conf.urls import url
from .views import StatusAPIView, StatusCreateAPIView, StatusDetailAPIView

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    re_path(r'^(?P<pk>.*)/$', StatusDetailAPIView.as_view()),
    # re_path(r'^(P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    # re_path(r'^(P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
]
