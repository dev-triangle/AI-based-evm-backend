from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from .models import (Student)
from .serializers import (StudentSerializer)
# Create your views here.

class StudentViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
