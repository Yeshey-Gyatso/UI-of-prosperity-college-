from django.db import models

# Create your models here.
class Users(models.Model):
    subject_name= models.CharField(max_length=20,unique=True)
    subject_id= models.PositiveIntegerField()

class Company(models.Model):
    Company_name= models.CharField(max_length=20,unique=True)


class Students(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20,null=True)
    TelePhone=models.PositiveIntegerField()
    Age=models.PositiveIntegerField()
    is_currently_student=models.BooleanField()
    # Subject = models.ForeignKey(Users,related_name='students',on_delete=models.CASCADE)
    # document = models.FileField(upload_to='documents/%Y/%m/%d/', null=True)
class Employee(models.Model):
    # Company_Name= models.ForeignKey(Company,related_name='employees',on_delete=models.CASCADE)
    Contact_Name=models.CharField(max_length=20)
    TelePhone=models.PositiveIntegerField()
    Company_Url=models.URLField(max_length=200)
    Type_Of_Business=models.CharField(max_length=20)
