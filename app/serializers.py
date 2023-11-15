from rest_framework import serializers
from .models import Post
from accounts.models import User
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200, required=False, allow_null=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id','username','email']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True) 
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author']



