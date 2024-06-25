from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly #작성자만 

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)