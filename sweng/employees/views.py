from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.http import HttpResponse, Http404



def home(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employees/home.html', context)

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return HttpResponse (employee)