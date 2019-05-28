from datetime import date

from django_filters import DateFilter, DateRangeFilter
from pusher import Pusher
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.utils import json
from django.http import JsonResponse, HttpResponse
from base import feedpermissions
from feeds.serializers import FeedSerializer
from .models import Feed
from django.views.decorators.csrf import csrf_exempt
from authen.models import Member
import requests

pusher = Pusher(app_id=u'783462', key=u'2ee37955973a41a7c708', secret=u'77b103e9955e8f46a2c0', cluster=u'ap3')


@action(detail=False, methods=['get'])
@csrf_exempt
def conversations(request):
    if feedpermissions:
        data = Feed.objects.all().order_by('-id')
        response = {}
        for feed in data:
            response[feed.id] = {'id': feed.id, 'name': feed.username, 'title': feed.title, 'content': feed.content,
                             'created': str(feed.created),
                             'updated': str(feed.updated),
                             'priority': feed.priority}
        return JsonResponse(json.dumps(response), safe=False)
    else:
        return HttpResponse(status=status.HTTP_403_FORBIDDEN)


@action(detail=False, methods=['post'])
@csrf_exempt
def broadcast(request):
    feed = Feed(title=request.POST.get('title', ''), content=request.POST.get('content', ''),
                creator=Member.objects.get(id=request.POST.get('id', '')),
                priority=request.POST.get('priority', ''), created=request.POST.get('created', ''))
    feed.save()
    response = {'id': feed.id, 'name': feed.username, 'title': feed.title, 'content': feed.content,
                         'created': str(feed.created), 'updated': str(feed.updated),
                         'priority': feed.priority}
    header = {"Content-Type": "application/json; charset=utf-8",
              "Authorization": "Basic ZTNmMDQ2YjUtMDc2NS00M2ZiLWJhNjYtMjkxY2EyMTljMjMy"}
    payload = {"app_id": "1d318c98-5b25-480c-89d9-5c5d265ffb53",
               "included_segments": ["All"],
               "contents": {"en": "New Feed", "ko": request.POST.get('title', '')},
               "url": "http://ec2-13-209-6-77.ap-northeast-2.compute.amazonaws.com/private/feeds"}
    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
    print(req.status_code, req.reason)
    pusher.trigger(u'a_channel', u'create_event', response)  # 이벤트 생성  -> 클라이어트로 전송 -> 모든 유저
    return JsonResponse(response, safe=False)


@action(detail=False, methods=['post'])
@csrf_exempt
def delivered(request, id):
    message = Feed.objects.get(pk=id)  # feed 게시판 index
    if request.POST.get('userIdx') != id:  # 액션을 받은 유저 index != 메세지를 생성한 유저 index
        socket_id = request.POST.get('socket_id', '')
        message.save()
        message = {'name': message.username, 'title': message.title, 'content': message.content,
                   'id': message.id, 'creator': message.creator.id, 'priority': message.priority}
        pusher.trigger(u'a_channel', u'delivered_message', message, socket_id)
        return HttpResponse('ok')
    else:
        return HttpResponse('Awaiting Delivery')


@action(detail=False, methods=['post'])
@csrf_exempt
def update(request, id):
    feed = Feed.objects.get(pk=id)
    data = request.POST
    response = FeedSerializer(feed, data=data, partial=True)
    if response.is_valid():
        response.save()
        response = {'id': feed.id, 'name': feed.username, 'title': feed.title, 'content': feed.content,
                          'created': str(feed.created), 'updated': str(feed.updated),
                          'priority': feed.priority}
        pusher.trigger(u'a_channel', u'updated_message', response)
    else:
        print(response.errors)
    return JsonResponse(response, safe=False)


@action(detail=False, methods=['post'])
@csrf_exempt
def delete(request, id):
    feed = Feed.objects.get(pk=id)  # feed 게시판 index
    feed.delete()
    response = {'id': feed.id, 'name': feed.username, 'title': feed.title, 'content': feed.content,
                         'created': str(feed.created), 'updated': str(feed.updated),
                         'priority': feed.priority}
    pusher.trigger(u'a_channel', u'deleted_message', response)  # 이벤트 생성  -> 클라이어트로 전송 -> 모든 유저
    return JsonResponse(response, safe=False)


# @action(detail=False, methods=['post'])
# @csrf_exempt
# def daterange():
#     Feed.filter(post_date__date=date.today())
