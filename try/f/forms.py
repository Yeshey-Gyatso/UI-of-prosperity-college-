from django import forms
from f.models import Students

class studentForm(forms.ModelForm):
    Name=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Enter your name",
        }))
    Email=forms.EmailField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Enter your name",
        }))
    TelePhone=forms.IntegerField(widget=forms.NumberInput(attrs={
        "class":"form-control",
        "placeholder":"Enter your number",
        }))
    Age=forms.IntegerField(widget=forms.NumberInput(attrs={
        "class":"form-control",
        "placeholder":"Enter your Age",
       }))


    class Meta:
        model = Students
        # fields='__all__'
        exclude = ['Subject']
