from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from celery_rest import views

router = routers.DefaultRouter()
router.register(r'periodic_tasks', views.PeriodicTaskViewSet)
router.register(r'interval_schedules', views.IntervalSchedulesViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += router.urls
