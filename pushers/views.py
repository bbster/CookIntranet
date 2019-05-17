from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from rest_framework.decorators import action
from feeds.models import Feed
from .models import *
from django.http import JsonResponse, HttpResponse

pusher = Pusher(app_id=u'783462', key=u'2ee37955973a41a7c708', secret=u'77b103e9955e8f46a2c0', cluster=u'ap3')


@action(detail=False, methods=['get'])
def conversations(request):
    data = Feed.objects.all()
    data = [{'name': feed.username, 'message': feed.content, 'id': feed.id} for
            feed in data]
    print(data)
    return JsonResponse(data, safe=False)


def broadcast(request):
    message = Feed(content=request.POST.get('content', ''), username=request.POST.get('username', ''))
    message.save()
    message = {'name': message.username, 'message': message.message, 'id': message.id}

    pusher.trigger(u'a_channel', u'an_event', message)
    return JsonResponse(message, safe=False)


def delivered(request, id):
    message = Conversation.objects.get(pk=id)
    # verify it is not the same user who sent the message that wants to trigger a delivered event
    if request.user.id != message.user.id:
        socket_id = request.POST.get('socket_id', '')
        message.status = 'Delivered'
        message.save()
        message = {'name': message.user.username, 'status': message.status, 'message': message.message,
                   'id': message.id}
        pusher.trigger(u'a_channel', u'delivered_message', message, socket_id)
        return HttpResponse('ok')
    else:
        return HttpResponse('Awaiting Delivery')
