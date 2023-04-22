from rest_framework import serializers
from .models import (Student,Candidate)


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Candidate
        fields='__all__'
    
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'