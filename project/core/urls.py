from django.contrib import admin
from django.urls import path

from tasks.views import get_status, home, run_task

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/<task_id>/", get_status, name="get_status"),
    path("tasks/", run_task, name="run_task"),
    path("", home, name="home"),
]
