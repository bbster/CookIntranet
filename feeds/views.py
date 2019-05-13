import requests
import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from base import feedpermissions
from feeds.serializers import FeedSerializer
from feeds.models import Feed


class FeedViewSet(ModelViewSet):
    queryset = Feed.objects.all().order_by('-id')
    serializer_class = FeedSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("creator", "created", "updated", "title", "content", "priority", "username")
    search_fields = ("creator", "created", "updated", "title", "content", "priority", "username")
    permission_classes = (feedpermissions.BasePermission,)

    @action(detail=False, methods=['GET'])
    def feedlist(self, request, *args, **kwargs):
        param_created_at = request.query_params.get('created', None)  # request.query_params -> request.GET
        if param_created_at:
            splited = param_created_at.split(",")  # 문자열 자름 #
            if len(splited) == 2:
                start_date = splited[0]
                end_date = splited[0]
                self.queryset = self.queryset.filter(created__range=(start_date, end_date))
            else:
                self.queryset = self.queryset.filter(created__date=splited[0])
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def createfeed(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        header = {"Content-Type": "application/json; charset=utf-8",
                  "Authorization": "Basic ZTNmMDQ2YjUtMDc2NS00M2ZiLWJhNjYtMjkxY2EyMTljMjMy"}
        payload = {"app_id": "1d318c98-5b25-480c-89d9-5c5d265ffb53",
                   "included_segments": ["All"],
                   "contents": {"en": "New Feed", "ko": request.data['title']},
                   "url": "http://ec2-13-209-6-77.ap-northeast-2.compute.amazonaws.com/private/feeds"}
        req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
        print(req.status_code, req.reason)
        return response

    # def updatefeed(self, request, *args, **kwargs):
    # return super().list(request, *args, **kwargs)
    #     id = self.get_object(creator_id)
    #     serializer = FeedSerializer(id, data=request.data)
    #     print(id, creator_id)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @detail_route(methods=['post'])
    # def deletefeed(self, request, pk, format=None):
    #     feed = self.get_object(pk)
    #     feed.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
