from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from .models import (User,Election,Candidate)
from .serializers import (RegisterSerializer,ElectionSerializer,CandidateSerializer)
""" from .AI_model.face_cnn import classifier,resultMap
 """
import base64
from django.http import JsonResponse
from PIL import Image
import numpy as np
import json

def recognize_face(request):
    print(request.POST)
    
"""  print(request.body)
    image_data = json.loads(request.body).get("image_data")
    image_binary=base64.b64decode(image_data)
    print(image_binary) """

""" ith open('test.jpg','wb') as f:
        f.write(image_binary)
    test_image=Image.open('test.jpg').convert('RGB').resize((64,64))
    test_image=np.array(test_image)/255.0
    test_image=np.expand_dims(test_image,axis=0)
    result=classifier.predict(test_image,verbose=0)
    predicted_name=resultMap[np.argmax(result)]
    return JsonResponse({'name':predicted_name})    """

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
    

