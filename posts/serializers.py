from rest_framework.serializers import ModelSerializer 
from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User

class PostSerializer(ModelSerializer):

    writer = serializers.ReadOnlyField(source = 'writer.username') 

    class Meta:
        model = Post
        fields = [ 'id', 'title', 'content', 'writer' ] #여기까지 게시글