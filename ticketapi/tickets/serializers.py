from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Ticket, Category


# Serializers define the API representation
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')

    

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('url', 'id','title', 'ticket_id','user', 'content', 'category', 'status', 'created', 'modified')


# Serializers define the API representation.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')





# ##### REWRITING SERIALIZERS MODELS MANUALLY
# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     username = serializers.CharField(max_length=200)
#     password = serializers.CharField(max_length=100, style={"input_type":"password"})
#     is_staff = serializers.BooleanField(default=False)

#     def create(self, validated_data):
#         """The function called when you create a new User object/instance"""

#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `User` instance, given the validated data.
#         """
#         instance.username = validated_data.get('username', instance.username)
#         instance.password = validated_data.get('password', instance.password)
#         instance.is_staff = validated_data.get('is_staff', instance.is_staff)
#         instance.save()
#         return instance
