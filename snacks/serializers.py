from rest_framework import serializers 
from .models import Snack,Post

class SnackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Snack
        # fields = '__all__'
        fields = ['id','owner','name','desc']

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['comment']