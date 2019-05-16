from django.http import JsonResponse
from pusher import Pusher
from requests import Response
from feeds.models import Feed


pusher = Pusher(app_id=u'783462', key=u'2ee37955973a41a7c708', secret=u'77b103e9955e8f46a2c0', cluster=u'ap3')

def test_message(self):
    message = Feed.objects.all()
    return Response(message)
    breakpoint()

def test_broadcast(request):
    # collect the message from the post parameters, and save to the database
    message = Feed(message=request.POST.get('message', ''), status='', user=request.user)
    message.save()
    # create an dictionary from the message instance so we can send only required details to pusher
    message = {'name': message.user.username, 'status': message.status, 'message': message.message, 'id': message.id}
    # trigger the message, channel and event to pusher
    pusher.trigger(u'a_channel', u'an_event', message)
    # return a json response of the broadcasted message
    return JsonResponse(message, safe=False)
