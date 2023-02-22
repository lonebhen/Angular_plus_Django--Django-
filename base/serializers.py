from rest_framework import serializers
from base.models import Departments, Employees



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        field = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        field = "__all__"