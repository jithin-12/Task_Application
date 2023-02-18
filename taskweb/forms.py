from django import forms
from django.contrib.auth.models import User
from api.models import Tasks

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
     

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class TaskForm(forms.ModelForm):
    
    class Meta:
        model=Tasks
        fields=["task_name"]
        widgets={
            "task_name":forms.TextInput(attrs={"class":"form-control"})
        }


class TaskEditForm(forms.ModelForm):
    class Meta:
        model=Tasks
        fields=["task_name","status"]