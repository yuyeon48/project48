from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    def create(self, validated_data):  
        user = User.objects.create_user(      
            username = validated_data['username'], 
            password = validated_data['password'], 
        )
        return user  
    class Meta: 
        model = User
        fields = [ 'username', 'password' ] 