from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from rest_framework.decorators import action
from authen.models import Member
from feeds.models import Feed
from django.http import JsonResponse, HttpResponse

pusher = Pusher(app_id=u'783462', key=u'2ee37955973a41a7c708', secret=u'77b103e9955e8f46a2c0', cluster=u'ap3')


@action(detail=False, methods=['get'])
def conversations(request):
    data = Feed.objects.all()
    data = [{'id': feed.id, 'name': feed.username, 'message': feed.content}
            for feed in data]
    return JsonResponse(data, safe=False)


@csrf_exempt
def broadcast(request):
    message = Feed(content=request.POST.get('content', ''), creator=Member.objects.get(id=request.POST.get('id', '')))
    message.save()
    message = {'name': message.username, 'message': message.content, 'id': message.id, 'creator': message.creator.id}
    pusher.trigger(u'a_channel', u'an_event', message)  # 이벤트 생성  -> 클라이어트로 전송 -> 모든 유저
    return JsonResponse(message, safe=False)


@action(detail=False, methods=['POST'])
@csrf_exempt
def delivered(request, id):
    message = Feed.objects.get(pk=id)  # feed 게시판 index
    if request.POST.get('userIdx') != id:   # 액션을 받은 유저 index != 메세지를 생성한 유저 index
        socket_id = request.POST.get('socket_id', '')
        message.save()
        message = {'name': message.username, 'message': message.content, 'id': message.id}
        pusher.trigger(u'a_channel', u'delivered_message', message, socket_id)
        return HttpResponse('ok')
    else:
        return HttpResponse('Awaiting Delivery')
