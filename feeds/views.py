from pusher import Pusher
from rest_framework.decorators import action
from rest_framework.utils import json
from django.http import JsonResponse, HttpResponse
from feeds.serializers import FeedSerializer
from .models import *
from django.views.decorators.csrf import csrf_exempt
from authen.models import Member
import requests

pusher = Pusher(app_id=u'783462', key=u'2ee37955973a41a7c708', secret=u'77b103e9955e8f46a2c0', cluster=u'ap3')


@action(detail=False, methods=['get'])
@csrf_exempt
def conversations(request):
    data = Feed.objects.all().order_by('-id')
    response = {}
    for feed in data:
        response[feed.id] = {'id': feed.id, 'name': feed.username, 'title': feed.title, 'content': feed.content,
                             'created': str(feed.created),
                             'updated': str(feed.updated),
                             'priority': feed.priority}

    return JsonResponse(json.dumps(response), safe=False)


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

    pusher.trigger(u'a_channel', u'an_event', response)  # 이벤트 생성  -> 클라이어트로 전송 -> 모든 유저
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
        pusher.trigger(u'a_channel', u'update_message', response)
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
