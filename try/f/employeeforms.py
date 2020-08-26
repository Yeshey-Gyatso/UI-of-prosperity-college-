from django import forms
from f.models import Employee

class employeeForm(forms.ModelForm):


    Contact_Name=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Enter your contact name",
            }))
    Company_Url=forms.URLField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Enter the url",
            }))
    TelePhone=forms.IntegerField(widget=forms.NumberInput(attrs={
            "class":"form-control",
            "placeholder":"Enter your number",
            }))
    Type_Of_Business=forms.CharField(widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Enter the type of business",
           }))

    class Meta:
        model = Employee
        fields='__all__'
