from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import (RegisterView,ElectionViewset,CandidateViewset,recognize_face,ImagerecViewset,test_face)

router=DefaultRouter()
router.register('register',RegisterView,basename='register')
router.register('election',ElectionViewset,basename='election')
router.register('candidates',CandidateViewset,basename='candidates')
router.register('imagerec',ImagerecViewset,basename='imagerec')
urlpatterns=[path('',include(router.urls)),
             path('recognize_face/', recognize_face, name='recognize_face'),
             path('test_face/',test_face,name='test_face'),
]
