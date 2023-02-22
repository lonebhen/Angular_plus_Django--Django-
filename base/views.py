from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers  import JSONParser
from django.http.response import  JsonResponse


from base.models import  Departments, Employees
from base.serializers import DepartmentSerializer, EmployeeSerializer


# Create your views here.
@csrf_exempt
def departmentAPI(request, id = 0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_seializer = DepartmentSerializer(departments, many = True)
        return JsonResponse(departments_seializer.data, safe=False)
    
    elif request.methd == 'POST':
        departments_data = JSONParser().parse(request)
        departments_seializer = DepartmentSerializer(data = departments_data)

        if departments_seializer.is_valid():
            departments_seializer.save()
            return JsonResponse("Department succesfully added", safe=False)
        else:
            return JsonResponse("Failed to add Department", safe=False)
        
    elif request.method == 'PUT':
        departments_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentID = departments_data['DepartmentID'])
        departments_seializer = DepartmentSerializer(department, data=departments_data)

        if departments_seializer.is_valid():
            departments_seializer.save()
            return JsonResponse("Department information Changed", safe=False)
        else:
            return JsonResponse("Failed to Update")
        
    elif request.method == 'DELETE':
        department =  Departments.objects.get(DepartmentID = id)
        department.delete()
        return JsonResponse("Succesfully Deleted")
        