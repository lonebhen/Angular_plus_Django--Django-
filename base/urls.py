from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from base import views

urlpatterns = [

    re_path(r'^departments$', views.departmentAPI),
    re_path(r'^departments/([0-9]+)$', views.departmentAPI),

    re_path(r'^employees$', views.employeeAPI),
    re_path(r'^employees/([0-9]+)$', views.employeeAPI),

    re_path(r'^employee/savefile', views.save_file)

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)