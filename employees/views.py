from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from employees.models import Employee

# Create your views here.

def employee_detail(request,pk):
    """ try:
            employee = Employee.objects.get(pk=pk)#pk is primary key
            print(employee)
            
    except:
            raise Http404"""
    #same as above
    employee = get_object_or_404(Employee,pk=pk)
    context = {
        'employee':employee,
    }
    return render(request, 'employee_details.html',context)