from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import (BlacklistTokenView,LoggedInUserView,RegisterView,UserDetailViewset,UserViewset,ElectionViewset,CandidateViewset,recognize_face,ImagerecViewset,test_face,VoteViewset,submit_vote)

router=DefaultRouter()
router.register('register',RegisterView,basename='register')
router.register('election',ElectionViewset,basename='election')
router.register('candidates',CandidateViewset,basename='candidates')
router.register('imagerec',ImagerecViewset,basename='imagerec')
router.register('vote',VoteViewset,basename='vote')
router.register('users',UserViewset,basename='users')
router.register('user-detail',UserDetailViewset,basename='user-detail')
urlpatterns=[path('',include(router.urls)),
             path('recognize_face/', recognize_face, name='recognize_face'),
             path('test_face/',test_face,name='test_face'),
             path('submit_vote/',submit_vote,name='submit_vote'),
             path('api/token/',TokenObtainPairView.as_view(),name="token_obtain"),
             path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
             path('api/token/blacklist/',BlacklistTokenView.as_view(),name="blacklist"),
             path('current-user/', LoggedInUserView.as_view(), name='currentuser'),
]
