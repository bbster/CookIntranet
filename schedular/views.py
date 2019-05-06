from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from base import schedulepermissions
from schedular.serializers import ScheduleSerializer
from .models import Schedules


class ScheduleViewSet(ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedules.objects.all()
    permission_classes = (schedulepermissions.BasePermission,)

    @action(detail=False, methods=['POST'])
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

    def createschedule(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def updateschedule(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def deleteschedule(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
