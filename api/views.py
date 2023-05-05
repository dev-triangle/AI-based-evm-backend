from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from .models import (User,Election,Candidate,Imagerec)
from .serializers import (RegisterSerializer,ElectionSerializer,CandidateSerializer,ImagerecSerializer)

""" from .AI_model.face_cnn import classifier,resultMap
 """ 
import base64
from django.http import JsonResponse,HttpResponse
""" from PIL import Image
 """
import numpy as np
import json
import io
from django.views.decorators.csrf import csrf_exempt
import os
import keras.utils as image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


""" def recognize_face(request):
           return HttpResponse("Welcome")
    
    print(request.body)
    image_data = json.loads(request.body).get("image_data")
    image_binary=base64.b64decode(image_data)
    print(image_binary) 

    with open('test.jpg','wb') as f:
        f.write(image_binary)
    test_image=Image.open('test.jpg').convert('RGB').resize((64,64))
    test_image=np.array(test_image)/255.0
    test_image=np.expand_dims(test_image,axis=0)
    result=classifier.predict(test_image,verbose=0)
    predicted_name=resultMap[np.argmax(result)]
    return JsonResponse({'name':predicted_name})  """   

@csrf_exempt
def recognize_face(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        # Save the uploaded image file to a temporary directory
        image_path = os.path.join(BASE_DIR, 'temp', 'hell.jpg')
        with open(image_path, 'wb') as f:
            f.write(image_file.read())
        # Load and preprocess the image
        test_image = image.load_img(image_path, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image /= 255.0
        print(test_image)
        print("hello")
        # Predict the class label
        """ result = classifier.predict(test_image)[0]
        predicted_class = result_map[np.argmax(result)] """
        # Remove the temporary image file
        os.remove(image_path)
        # Return the predicted class label as a response
        """         return HttpResponse(predicted_class)
        """    
    else:
        return render(request, 'recognize_image.html')

""" def recognize_face(request):
    image_data = json.loads(request.body).get("image_data")
    print(image_data)
    image_binary = base64.b64decode(image_data)

    with io.BytesIO(image_binary) as stream:
        stream.seek(0)
        test_image = Image.open(stream).convert('RGB').resize((64,64))
        test_image = np.array(test_image) / 255.0
        test_image = np.expand_dims(test_image, axis=0) 
        result = classifier.predict(test_image, verbose=0)
        predicted_name = resultMap[np.argmax(result)] """



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
    
class ImagerecViewset(viewsets.ModelViewSet):
    queryset=Imagerec.objects.all()
    serializer_class=ImagerecSerializer
    
    def post(self,request,*args,**kwargs):
        cover=request.data['cover']
        title=request.data['title']
        Imagerec.objects.create(title=title,cover=cover)
        return HttpResponse({'message': 'image created'},status=200)
