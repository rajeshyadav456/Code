from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from app import views
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'api/post', PostViewSet,basename='post')

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),   


]+router.urls




