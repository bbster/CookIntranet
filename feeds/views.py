from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from base import feedpermissions
from feeds.serializers import FeedSerializer
from feeds.models import Feed


class FeedViewSet(ModelViewSet):
    queryset = Feed.objects.all().order_by('-id')
    serializer_class = FeedSerializer
    permission_classes = (feedpermissions.BasePermission,)

    @action(detail=False, methods=['GET'])
    def feedlist(self, request, *args, **kwargs):
        param_created_at = request.query_params.get('created', None)  # request.query_params -> request.GET
        if param_created_at:
            splited = param_created_at.split(",")  # 문자열 자름 #
            if len(splited) == 2:
                start_date = splited[0]
                end_date = splited[0]
                self.queryset = self.queryset.filter(created_date__range=(start_date, end_date))
            else:
                self.queryset = self.queryset.filter(created_date__date=splited[0])
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def createfeed(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def updatefeed(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def deletefeed(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
