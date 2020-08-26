from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from f.models import Users,Students
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models
from f.forms import studentForm
from f.employeeforms import employeeForm
#
def index(request):
    d={'hi':"wassupp"}
    return render(request,'f/index.html',context=d)
# def data(request):
#     n=Users.objects
#     return render(request,'f/index.html',{'name':n})
def studentform(request):
    form=studentForm()
    if request.method=="POST":
        form=studentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect(reverse("index"))
            else:
                print(form.errors)
            # return index(request)
    return render(request,'f/student_forms.html',{'form':form})

def employeeform(request):
    form_e=employeeForm()
    if request.method=="POST":
        form_e=employeeForm(request.POST)
        if form_e.is_valid():
            form_e.save(commit=True)
            return HttpResponseRedirect(reverse("index"))
            # return index(request)
        else:
            print(form_e.errors)
    return render(request,'f/employee.html',{'form_e':form_e})

def base(request):
    d={'hi':"wassupp"}
    return render(request,'f/base.html',context=d)


def aboutus(request):
    d={'hi':"wassupp"}
    return render(request,'f/aboutus.html',context=d)

def contactus(request):
    d={'hi':"wassupp"}
    return render(request,'f/contactus.html',context=d)

def courses(request):
    d={'hi':"wassupp"}
    return render(request,'f/courses.html',context=d)

def slider(request):
    d={'hi':"wassupp"}
    return render(request,'f/slider.html',context=d)
# Create your views here
