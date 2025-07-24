from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse
from . models import Employees

# Create your views here.

def employee_details(request,pk):
    context = {
        'employee' : get_object_or_404(Employees,pk=pk),
    }
    return render(request,'emp.html',context)
