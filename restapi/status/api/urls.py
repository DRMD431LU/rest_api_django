from django.urls import path, include, re_path
from .views import StatusAPIView, StatusCreateAPIView

urlpatterns = [
    path('api', StatusAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    # re_path(r'^(P<id>.*)/$', StatusCreateAPIView.as_view()),
    # re_path(r'^(P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    # re_path(r'^(P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
]
