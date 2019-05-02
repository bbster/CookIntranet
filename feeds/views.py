# # feeds/views.py
# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from feeds.serializers import FeedSerializers
# from base.permissions import BasePermission
# from .models import Feed
#
# class FeedList(viewsets.ModelViewSet):
#     serializer_class = FeedSerializers
#     queryset = Feed.objects.all()
#
#     @action(detail=False, methods=['POST'])
#     def list(self, request, *args, **kwargs):
#         feed_title = request.get.data("Title", None) # feed title 불러옴
#
#
# class FeedViewSet(viewsets.ModelViewSet):
#     # 회원가입을 할땐, 권한 체크 X
#     serializer_class = FeedSerializers
#     queryset = Feed.objects.all()
#     # permission_classes = (BasePermission, )
#
#     @action(detail=False, methods=['POST'])
#     def login(self, request, *args, **kwargs):
#         username = request.data.get("username", None)
#         password = request.data.get("password", None)
#         user = authenticate(username=username, password=password)
#
#         # LOGIN 할때 JWT TOKEN 발급
#         if user is not None:
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             # JWT TOKEN RESPONSE
#             return Response({"token": token}, status=200)
#         else:
#             return Response({'Error': "ERROR"}, status=400)
#
# class ListFeed(generics.ListCreateAPIView):
#     queryset = Feed.Feed.objects.all()
#     serializer_class = serializers.TodoSerializer
#
#
# class DetailFeed(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Feed.objects.all()
#     serializer_class = serializers.TodoSerializer
