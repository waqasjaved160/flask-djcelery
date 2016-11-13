from djcelery.models import IntervalSchedule, PeriodicTask
from rest_framework import viewsets

from celery_rest.serializers import PeriodicTaskSerializer, IntervalScheduleSerializer


class PeriodicTaskViewSet(viewsets.ModelViewSet):
    """
        Define the periodic tasks
    """
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer


class IntervalSchedulesViewSet(viewsets.ModelViewSet):
    """
        Define all the intervals for the jobs
        e.g 30 seconds, 1 minute, 1 hour etc
    """
    queryset = IntervalSchedule.objects.all()
    serializer_class = IntervalScheduleSerializer
