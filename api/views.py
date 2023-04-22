from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from .models import (Student,Candidate)
from .serializers import (StudentSerializer,CandidateSerializer)
# Create your views here.

class CandidateViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer
    
class StudentViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
