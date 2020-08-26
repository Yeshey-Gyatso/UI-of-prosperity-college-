"""try URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from f import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name='base'),
    path('student/',views.studentform,name='student_forms'),
    path('employee/',views.employeeform,name='employee_forms'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('index/',views.index,name='index'),
    path('contactus/',views.contactus,name='contactus'),
    path('courses/',views.courses,name="courses"),
    path('slider/',views.slider,name="slider"),
    # path('base/',views.base,name='base'),
]