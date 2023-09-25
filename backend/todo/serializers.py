from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.completed = validated_data.get("completed", instance.completed)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = Users
            fields = "__all__"