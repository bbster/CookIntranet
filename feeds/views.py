import requests
import json
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
        response = super().create(request, *args, **kwargs)
        header = {"Content-Type": "application/json; charset=utf-8",
                  "Authorization": "Basic ZTNmMDQ2YjUtMDc2NS00M2ZiLWJhNjYtMjkxY2EyMTljMjMy"}
        payload = {"app_id": "1d318c98-5b25-480c-89d9-5c5d265ffb53",
                   "included_segments": ["All"],
                   "contents": {"en": "New Feed", "ko": request.data['title']},
                   "headings": {"en": "New Feed", "ko": request.data['username']},
                   "url": "http://ec2-13-209-6-77.ap-northeast-2.compute.amazonaws.com/private/feeds"}
        req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
        print(req.status_code, req.reason)
        return response

    @action(detail=False, methods=['post'])
    def updatefeed(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def deletefeed(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
