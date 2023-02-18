from rest_framework import serializers
from api.models import Tasks
from django.contrib.auth.models import User


#localhost:8000/users/
#post
#data=("username":"abc","password":"123",

class TaskSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    created_date=serializers.DateTimeField(read_only=True)
    status=serializers.BooleanField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Tasks
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password","first_name","last_name"]
