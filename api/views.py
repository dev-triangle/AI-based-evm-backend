from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from .models import (User,Election,Candidate,Imagerec)
from .serializers import (RegisterSerializer,ElectionSerializer,CandidateSerializer,ImagerecSerializer)

# from .AI_model.face_cnn import classifier,resultMap
 
import base64
from django.http import JsonResponse,HttpResponse
""" from PIL import Image
 """
import numpy as np
import json
import io
from django.views.decorators.csrf import csrf_exempt
import os
import face_recognition
import numpy as np
import csv
from datetime import datetime
import cv2
import base64
from sklearn import svm
# import keras.utils as image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'media'))

@csrf_exempt
def test_face(request):
    body_unicode = request.body.decode('utf-8')
    body_data = json.loads(body_unicode)
    imagedata = body_data['imagedata']
    print(imagedata)
    imagedata = imagedata.split(',')[1].strip()  

    decoded_img=base64.b64decode((imagedata))
    img_file=open('media/covers/image.jpeg','wb')
    img_file.write(decoded_img)
    img_file.close()
    return HttpResponse("welcome")

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
  image_path1=os.path.join(BASE_DIR,"AI_model","ImagesAttendance","image_testing","adithya","adithya.jpeg")
  image_path2=os.path.join(BASE_DIR,"AI_model","ImagesAttendance","image_testing","sanosh","sanosh.jpeg")

  ema_img=face_recognition.load_image_file(image_path1)
  ema_encoding=face_recognition.face_encodings(ema_img)[0]

  bezos_img=face_recognition.load_image_file(image_path2)
  bezos_encoding=face_recognition.face_encodings(bezos_img)[0]
  known_face_encoding=[
    ema_encoding,bezos_encoding
  ]

  known_face_names=[
    "Adithya","sanosh"
  ]
  clf=svm.SVC()
  clf.fit(known_face_encoding,known_face_names)
  valid_voters=known_face_names.copy()

  face_locations = []
  face_encodings = []
  face_names = []
  s =True
  image_path=os.path.join(MEDIA_ROOT,"covers","image.jpeg")
  frame=cv2.imread(image_path)
  small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
  rgb_small_frame = small_frame[:,:,::-1]
  name=""
  if s:
      face_locations=face_recognition.face_locations(small_frame)
      face_encodings=face_recognition.face_encodings(small_frame,face_locations)
      face_names=[]
      for face_encoding in face_encodings:
        name = clf.predict([face_encoding])
        print(name[0])
  return JsonResponse({'voter_name': name[0]})
# def recognize_face(request):
#   image_path1=os.path.join(BASE_DIR,"AI_model","ImagesAttendance","image_testing","adithya","adithya.jpeg")
#   image_path2=os.path.join(BASE_DIR,"AI_model","ImagesAttendance","image_testing","sanosh","sanosh.jpeg")

#   ema_img=face_recognition.load_image_file(image_path1)
#   ema_encoding=face_recognition.face_encodings(ema_img)[0]

#   bezos_img=face_recognition.load_image_file(image_path2)
#   bezos_encoding=face_recognition.face_encodings(bezos_img)[0]

# # kristen_img=face_recognition.load_image_file('./sample_images/kristen.jpeg')
# # kristen_encoding=face_recognition.face_encodings(kristen_img)[0]

# # # elon_img=face_recognition.load_image_file('./sample_images/')
# # hari_img=face_recognition.load_image_file('./sample_images/hari.jpeg')
# # hari_encoding=face_recognition.face_encodings(hari_img)[0]

# # nandu_img=face_recognition.load_image_file('./sample_images/nandv.jpeg')
# # nandu_encoding=face_recognition.face_encodings(nandu_img)[0]

# # alen_img=face_recognition.load_image_file('./sample_images/alen.jpeg')
# # alen_encoding=face_recognition.face_encodings(alen_img)[0]

#   known_face_encoding=[
#     ema_encoding,bezos_encoding
#   ]

#   known_face_names=[
#     "Adithya","sanosh"
#   ]
  
#   valid_voters=known_face_names.copy()

#   face_locations = []
#   face_encodings = []
#   face_names = []
#   s =True

#   now=datetime.now()
#   current_date = now.strftime("%Y-%m-%d")

#   f = open(current_date+'.csv','w+',newline = '')
#   cswriter=csv.writer(f)

#   image_path=os.path.join(MEDIA_ROOT,"covers","image.jpeg")
#   frame=cv2.imread(image_path)
#   small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
#   rgb_small_frame = small_frame[:,:,::-1]
#   validname=""
#   if s:
#       face_locations=face_recognition.face_locations(small_frame)
#       face_encodings=face_recognition.face_encodings(small_frame,face_locations)
#       face_names=[]

#       for face_encoding in face_encodings:
#           matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
#           face_distance=face_recognition.face_distance(known_face_encoding,face_encoding)
#           best_index=np.argmin(face_distance)
#           name=""
#           if matches[best_index]:
#               name=known_face_names[best_index]
#           face_names.append(name)

#           if name in known_face_names:
#               if name in valid_voters:
#                   valid_voters.remove(name)
#                   print(valid_voters)
#                   print(name)
#                   validname=name
#                   current_time=now.strftime("%H-%M-%S")
#                   cswriter.writerow([name,current_time])
  
#   f.close()
#   return JsonResponse({'name':validname})
#   print("c0de completed")        

# def recognize_face(request):
#     if request.method == 'GET':
#         """ image_file = request.FILES['image'] """
#         # Save the uploaded image file to a temporary directory

#         image_path = os.path.join(MEDIA_ROOT, 'covers', 'hi', 'aaamm.jpg')
#         """ with open(image_path, 'wb') as f:
#             f.write(image_file.read()) """
#         # Load and preprocess the image
#         test_image = image.load_img(image_path, target_size=(64, 64))
#         test_image = image.img_to_array(test_image)
#         test_image = np.expand_dims(test_image, axis=0)
#         """ test_image /= 255.0 """
#         print(test_image)
#         print("hello")
#         # Predict the class label
#         result = classifier.predict(test_image,verbose=0)
#         predicted_class = resultMap[np.argmax(result)]
#         # Remove the temporary image file
#         """ os.remove(image_path) """
#         # Return the predicted class label as a response
#         return HttpResponse(predicted_class)
            
#     else:
#         return render(request, 'recognize_image.html')

#  def recognize_face(request):
#     image_data = json.loads(request.body).get("image_data")
#     print(image_data)
#     image_binary = base64.b64decode(image_data)

#     with io.BytesIO(image_binary) as stream:
#         stream.seek(0)
#         test_image = Image.open(stream).convert('RGB').resize((64,64))
#         test_image = np.array(test_image) / 255.0
#         test_image = np.expand_dims(test_image, axis=0) 
#         result = classifier.predict(test_image, verbose=0)
#         predicted_name = resultMap[np.argmax(result)] 



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
