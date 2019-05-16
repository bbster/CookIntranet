import requests
import json
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from base import feedpermissions
from feeds.serializers import FeedSerializer
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from .models import *
from django.http import JsonResponse, HttpResponse


class FeedViewSet(ModelViewSet):
    queryset = Feed.objects.all().order_by('-id')
    serializer_class = FeedSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("creator", "created", "updated", "title", "content", "priority", "username")
    search_fields = ("creator", "created", "updated", "title", "content", "priority", "username")
    permission_classes = (feedpermissions.BasePermission,)
    pusher = Pusher(app_id=u'783462', key=u'2ee37955973a41a7c708', secret=u'77b103e9955e8f46a2c0', cluster=u'ap3')

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
                # data = Feed.objects.all()
                # data = [{'name': person.user.username, 'status': person.status, 'message': person.message,
                #         'id': person.id} for person in data]
                # return JsonResponse(data, safe=False)

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

        # message = Feed(message=request.POST.get('message', ''), status='', user=request.user)
        # message.save()
        # # create an dictionary from the message instance so we can send only required details to pusher
        # message = {'name': message.user.username, 'status': message.status, 'message': message.message,
        #            'id': message.id}
        # # trigger the message, channel and event to pusher
        # pusher.trigger(u'a_channel', u'an_event', message)
        # # return a json response of the broadcasted message
        # return HttpResponse(json.dumps(message), content_type="application/json", safe=False)

    @csrf_exempt
    def delivered(self, request, id):
        message = Feed.objects.get(pk=id)
        # verify it is not the same user who sent the message that wants to trigger a delivered event
        if request.user.id != message.user.id:
            socket_id = request.POST.get('socket_id', '')
            message.status = 'Delivered'
            message.save()
            message = {'name': message.user.username, 'status': message.status, 'message': message.message, 'id': message.id}
            pusher.trigger(u'a_channel', u'delivered_message', message, socket_id)
            return HttpResponse('ok')
        else:
            return HttpResponse('Awaiting Delivery')

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

    # def feedhit(self, request, ip=None, creator=None, *args, **kwargs):
    #     try:
    #         # ip주소와 게시글 번호로 기록을 조회함
    #         hits = HitCount.objects.get(ip=ip, post=post)
    #     except Exception as e:
    #         # 처음 게시글을 조회한 경우엔 조회 기록이 없음
    #         print(e)
    #         hits = HitCount(ip=ip, post=post)
    #         Feed.objects.filter(attachment_ptr_id=creator).update(hits=post.hits + 1)
    #         hits.save()
    #     else:
    #         # 조회 기록은 있으나, 날짜가 다른 경우
    #         if not hits.date == timezone.now().date():
    #             Feed.objects.filter(attachment_ptr_id=creator).update(hits=post.hits + 1)
    #             hits.date = timezone.now()
    #             hits.save()
    #         # 날짜가 같은 경우
    #         else:
    #             print(str(ip) + ' has already hit this post.\n\n')
    #
    # @action(detail=False, methods=['post', 'delete'])
    # def like(self, request):
    #     title = request.data.get("title", None)
    #     with transaction.atomic():
    #         try:
    #             user = Feed.objects.select_for_update().get(username=request.username, title=title)
    #         except:
    #             return Response(status=status.HTTP
