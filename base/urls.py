from django.urls import re_path

from base import views

urlpatterns = [

    re_path(r'^departments$', views.departmentAPI),
    re_path(r'^departments/([0-9]+)$', views.departmentAPI),

    re_path(r'^employees$', views.employeeAPI),
    re_path(r'^employees/([0-9]+)$', views.employeeAPI)

]