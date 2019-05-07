from django.shortcuts import redirect
from requests import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from base import feedpermissions
from feeds.serializers import FeedSerializer
from feeds.models import Feed


class FeedViewSet(ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = (feedpermissions.BasePermission,)

    @action(detail=False, methods=['GET'])
    def feedlist(self, request, *args, **kwargs):
        param_created_at = request.query_params.get('created_at', None)  # request.query_params -> request.GET
        if param_created_at:
            splited = param_created_at.split(",")
            if len(splited) == 2:
                start_date = splited[0]
                end_date = splited[0]
                self.queryset = self.queryset.filter(created_date__range=(start_date, end_date))
            else:
                self.queryset = self.queryset.filter(created_date__date=splited[0])
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['POST'])
    def createfeed(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['POST'])
    def updatefeed(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['POST'])
    def deletefeed(self, request, pk=None, *args, **kwargs):
        return super().destroy(request, pk, *args, **kwargs)

    # def update(self, pk, request, *args, **kwargs):
    #     id = Feed.objects.pop('id', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, pk=id)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)