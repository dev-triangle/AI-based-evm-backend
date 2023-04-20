from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import (StudentViewset)

router=DefaultRouter()
router.register('students',StudentViewset,basename='students')
urlpatterns=[path('',include(router.urls))]