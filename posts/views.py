from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet 

class PostViewSet(ModelViewSet): 
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer): 
        serializer.save(writer = self.request.user)