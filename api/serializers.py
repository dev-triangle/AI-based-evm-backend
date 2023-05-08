from rest_framework import serializers
from .models import (User,Election,Candidate,Imagerec,Vote,UserDetail)
from rest_framework.permissions import IsAuthenticated

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    permission_classes=[IsAuthenticated]
    class Meta:
        model=User
        fields=['email','username','password','id']

    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError("username should contain only alpha numeric chars")
        return attrs

    def create(self,validated_data):
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
    class Meta:
        model=User
        fields=['id','username','email']
        
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vote
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    user_image=serializers.ImageField(max_length=None,allow_empty_file=False,use_url=True,required=False)
    class Meta:
        model=UserDetail
        fields='__all__'        