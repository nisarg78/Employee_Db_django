import datetime
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context
from django.db.models import Q

import emp
from .models import *


def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request, 'all_emp.html',context)

def add_emp(request):

    if request.method == 'POST':
        first_name = str(request.POST['first_name'])
        last_name = str(request.POST['last_name'])
        dept= request.POST['dept']
        
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        phone = int(request.POST['phone'])
        print(first_name,last_name,dept)
        Employee(first_name = first_name, last_name=last_name, dept = Department.objects.filter(id = dept).first(), phone = phone, salary=salary, bonus=bonus, role = Role.objects.filter(id = role).first(), hire_date = datetime.datetime.now()).save()
        
        msg="Data Stored Successfully"
        return render(request,"index.html",{'msg':msg})
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('Problem Ocuured! No Data Insert')

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return render(request,"index.html")
            # return HttpResponse("Employe Remove Successfully")
        except:
            return HttpResponse("Please Enter A Valid Emp Id")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request, 'remove_emp.html', context)

def fillter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains =dept)
        if role:
            emps = emps.filter(role__name__icontains =role)
            
        context = {
            'emps': emps
        }
        
        return render(request, 'all_emp.html',context)
    elif request.method == 'GET':                    
        return render(request, 'fillter_emp.html')
    else:
        return HttpResponse('Error For Filter')
