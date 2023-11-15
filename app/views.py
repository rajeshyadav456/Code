from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from rest_framework import status

from .models import Post
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from accounts.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import IsCurrentUserOwnerOrReadOnly
from .mypagination import CustomPageNumberPagination
# Create your views here.





class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes=[IsCurrentUserOwnerOrReadOnly,]
    pagination_class = CustomPageNumberPagination


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.query_params.get('order_by')
        meta_title = self.request.query_params.get('meta_title', None)
        title=self.request.query_params.get('title',None)
        body=self.request.query_params.get('body',None) 
        author_username=self.request.query_params.get('author_username',None)       
        if title:
            queryset = queryset.filter(title__icontains=title)
        if body:
            queryset = queryset.filter(body__icontains=body)  
        
        if author_username:
            queryset = queryset.filter(author__username__icontains=author_username)
       
        return queryset
