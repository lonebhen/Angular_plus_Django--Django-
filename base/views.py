from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers  import JSONParser
from django.http.response import  JsonResponse
from django.core.files.storage import default_storage


from base.models import  Departments, Employees
from base.serializers import DepartmentSerializer, EmployeeSerializer


# Create your views here.
@csrf_exempt
def departmentAPI(request, id = 0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many = True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        departments_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data = departments_data)

        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Department succesfully added", safe=False)
        else:
            return JsonResponse("Failed to add Department", safe=False)
        
    elif request.method == 'PUT':
        departments_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId = departments_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department, data=departments_data)

        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Department information Changed", safe=False)
        else:
            return JsonResponse("Failed to Update")
        
    elif request.method == 'DELETE':
        department =  Departments.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Succesfully Deleted", safe=False)
    

@csrf_exempt

def employeeAPI(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many= True)
        return JsonResponse(employees_serializer.data, safe=False)
    
    elif request.method == 'POST':
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employees_data)

        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Employee added succesfully", safe=False)
        return JsonResponse("Failed to add employee", safe=False)
    
    elif request.method == 'PUT':
        employees_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId = employees_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employee, data=employees_data)

        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Succesfully changed employee information", safe= False)
        return JsonResponse("Failed to upgrade employee data", safe=False)
    
    elif request.method == 'DELETE':
        employee  = Employees.objects.get(EmployeeId = id)
        employee.delete()
        return JsonResponse("Succesfully Deleted Employee", safe=False)
    

@csrf_exempt
def save_file(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


