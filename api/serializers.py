from rest_framework import serializers
from .models import (User,Election,Candidate,Imagerec)
from rest_framework.permissions import IsAuthenticated

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    voters_id = serializers.CharField(max_length=50)
    aadhaar_number = serializers.CharField(max_length=12)
    username=serializers.CharField()
    user_img = serializers.ImageField()
    permission_classes=[IsAuthenticated]
    
    class Meta:
        model = User
        fields = ['email', 'password','username', 'voters_id', 'aadhaar_number', 'user_img']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username=attrs.get('username','')
        voters_id=attrs.get('voters_id','')
        aadhaar_number=attrs.get('aadhaar_number','')
        user_img=attrs.get('user_img','')
        
                            
       

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Election
        fields='__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Candidate
        fields='__all__'
    
class ImagerecSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Imagerec
        fields='__all__'   

class UserSerializer(serializers.ModelSerializer):
    voters_id = serializers.CharField(max_length=50, read_only=True)
    aadhaar_number = serializers.CharField(max_length=12, read_only=True)
    user_img = serializers.ImageField(read_only=True,allow_empty_file=True)
    username = serializers.CharField(max_length=50, read_only=True)

    class Meta:
        model = User
        fields = '__all__'