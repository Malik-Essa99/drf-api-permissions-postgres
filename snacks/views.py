from django.shortcuts import render
from .models import Snack,Post
from rest_framework.generics import ListAPIView,RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import SnackSerializer,PostSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from .permissions import IsOwnerOrReadOnly,IsAnAdminOrStaffUser


########### Snack ###########

class SnackListView(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = [IsAuthenticated]

class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = [IsOwnerOrReadOnly]

########### Post ###########

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
# Added this permission so that only the admins can update and delete the posts, any other user or non user can only view the posts

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAnAdminOrStaffUser]
    
    