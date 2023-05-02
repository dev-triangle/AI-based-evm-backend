from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from .models import (User,Election,Candidate)
from .serializers import (RegisterSerializer,ElectionSerializer,CandidateSerializer)
# Create your views here.
class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()

class ElectionViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=Election.objects.all()
    serializer_class=ElectionSerializer

class CandidateViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer
    

