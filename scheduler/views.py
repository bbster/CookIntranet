from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from base import schedulepermissions
from scheduler.serializers import ScheduleSerializer
from .models import Schedules


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedules.objects.all().order_by('-id')
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("creator", "created", "updated", "title", "detail", "username")
    search_fields = ("creator", "created", "updated", "title", "detail", "username")
    permission_classes = (schedulepermissions.BasePermission,)

    @action(detail=False, methods=['GET'])
    def schedulelist(self, request, *args, **kwargs):
        param_created_at = request.query_params.get('created_at', None)  # request.query_params -> request.GET
        if param_created_at:
            splited = param_created_at.split(",")
            if len(splited) == 2:
                start_date = splited[0]
                end_date = splited[0]
                self.queryset = self.queryset.filter(created_date__range=(start_date, end_date))
            else:
                self.queryset = self.queryset.filter(created_date__date=splited[0])
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['POST'])
    def createschedule(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # @action(detail=False, methods=['POST'])
    # def updateschedule(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # @action(detail=False, methods=['POST'])
    # def deleteschedule(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)
