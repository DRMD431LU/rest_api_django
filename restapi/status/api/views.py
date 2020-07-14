import json
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializer


def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

class StatusAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
#    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None) or self.passed_id
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def perform_destroy(self, instance):
        if instance is not None:
            return instance.delete()
        return None

    def get(self, request, *args, **kw):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None or passed_id is not "":
            return self.retrieve(request, *args, **kw)
        return super().get(request, *args, **kw)

    def post(self, request, *args, **kw):
        return self.create(request, *args, **kw)

#    def perform_create(self, serializer):
#        serializer.save(user=self.reques.usr)

    def patch(self, request, *args, **kw):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None or passed_id is not "":
            return self.retrieve(request, *args, **kw)
        return super().get(request, *args, **kw)

    def put(self, request, *args, **kw):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None or passed_id is not "":
            return self.retrieve(request, *args, **kw)
        return super().get(request, *args, **kw)

    def delete(self, request, *args, **kw):
        url_passed_id = request.GET.get('id', None)
        json_data = {}
        body_ = request.body
        if is_json(body_):
            json_data = json.loads(request.body)
        new_passed_id = json_data.get('id', None)
        passed_id = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None or passed_id is not "":
            return self.retrieve(request, *args, **kw)
        return super().get(request, *args, **kw)




















# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []
#
#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     # def post(self, request, format=None):
#     #         qs = Status.objects.all()
#     #         serializer = StatusSerializer(qs, many=True)
#     #         return Response(serializer.data)
#
#
# class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#
#     def put(self, request, *args, **kw):
#         return self.update(request, *args, **kw)
#
#     def delete(self, request, *args, **kw):
#         return self.destroy(request, *args, **kw)
#
#
# # class StatusUpdateAPIView(generics.UpdateAPIView):
# #     permission_classes = []
# #     authentication_classes = []
# #     queryset = Status.objects.all()
# #     serializer_class = StatusSerializer
#
#
# # class StatusDeleteAPIView(generics.DestroyAPIView):
# #     permission_classes = []
# #     authentication_classes = []
# #     queryset = Status.objects.all()
# #     serializer_class = StatusSerializer
