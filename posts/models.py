from django.db import models
from django.contrib.auth.models import User

class Post(models.Model) : 
    title = models.CharField(verbose_name="제목", max_length=128)
    content = models.TextField(verbose_name="내용", default='') 
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

    
    def __str__(self):
        return self.title
    

