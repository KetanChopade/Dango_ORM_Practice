from django.shortcuts import render
from app1.models import Person


def showindex(request):
    qs = Person.objects.all()       #for feching all from database
    data = {"all":qs}
    return render(request,"index.html",data)

def showindex(request):
    qs = Person.objects.only('name','age')       #for feching only from database
    data = {"only":qs}
    return render(request,"index.html",data)

def showindex(request):
    qs = Person.objects.all()[:3]       #Fetch specific number of rows
    data = {"limit":qs}
    return render(request,"index.html",data)

def showindex(request):
    qs = Person.objects.all()[3:7]       #Fetch LIMIT AND OFFSET keywords
    data = {"limit":qs}
    return render(request,"index.html",data)

def showindex(request):
    qs = Person.objects.filter(idno=1)     #Filter by single column
    data = {"filter":qs}
    return render(request,"index.html",data)

def showindex(request):             #Filter by comparison operators
    qs =  Person.objects.filter(age__gt=27)     #Person.objects.filter(age__lt=18)
    data = {"age":qs}                           #Person.objects.filter(age__gte=18)     #Person.objects.filter(age__lte=18)
    return render(request,"index.html",data)    ##Person.objects.exclude(age=18)

def showindex(request):
    qs = Person.objects.filter(age__range=(27, 30))     #Filter by BETWEEN/range Clause
    data = {"range":qs}
    return render(request,"index.html",data)

def showindex(request):
    qs = Person.objects.filter(name__icontains='k')     #Filter by LIKE operator
    data = {"contains":qs}                              #IN operator      Person.objects.filter(id__in=[1, 2])
    return render(request,"index.html",data)