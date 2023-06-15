from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from .models import (User,Election,Candidate,Imagerec,Vote,UserDetail)
from .serializers import (RegisterSerializer,UserDetailSerializer,ElectionSerializer,CandidateSerializer,ImagerecSerializer,UserSerializer,VoteSerializer)
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
# from .AI_model.face_cnn import classifier,resultMap
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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
# from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier

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
    # Load known face encodings and names from image files
    image_path1 = os.path.join(BASE_DIR, "AI_model", "ImagesAttendance", "image_testing", "adithya", "adithya.jpeg")
    image_path2 = os.path.join(BASE_DIR, "AI_model", "ImagesAttendance", "image_testing", "sanosh", "sanosh.jpeg")
    # image_path3 = os.path.join(BASE_DIR, "AI_model", "ImagesAttendance", "image_testing", "arjun", "arjun.jpeg")
    image_path4 = os.path.join(BASE_DIR, "AI_model", "ImagesAttendance", "image_testing", "nandu", "nandu.jpeg")
    ema_img = face_recognition.load_image_file(image_path1)
    ema_encoding = face_recognition.face_encodings(ema_img)[0]
    bezos_img = face_recognition.load_image_file(image_path2)
    bezos_encoding = face_recognition.face_encodings(bezos_img)[0]
    # arjun_img = face_recognition.load_image_file(image_path3)
    # arjun_encoding = face_recognition.face_encodings(arjun_img)[0]
    nandu_img = face_recognition.load_image_file(image_path4)
    nandu_encoding = face_recognition.face_encodings(nandu_img)[0]
    
    known_face_encoding = [
        ema_encoding, bezos_encoding , nandu_encoding
    ]
    known_face_names = [
        "Adithya", "sanosh","Nandu"
    ]
    
    # Load list of valid voters from a file
    valid_voters_path = os.path.join(BASE_DIR, "valid_voters.json")
    with open(valid_voters_path, "r") as f:
        valid_voters = json.load(f)
    
    # # Train classifier on known face encodings and names
    # clf = svm.SVC()
    # clf.fit(known_face_encoding, known_face_names)
    # Train classifier on known face encodings and names
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(known_face_encoding, known_face_names)
    
    # Detect faces in the image and recognize voters
    face_locations = []
    face_encodings = []
    face_names = []
    s = True
    image_path = os.path.join(MEDIA_ROOT, "covers", "image.jpeg")
    frame = cv2.imread(image_path)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    for voter in valid_voters:
        if voter["voted"] == False:
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                name = clf.predict([face_encoding])[0]
                if name == voter["name"]:
                    voter["voted"] = True
                    with open(valid_voters_path, "w") as f:
                        json.dump(valid_voters, f)
                    return JsonResponse({'voter_name': name})
    
    # If no valid voters are found, return an error message
    return JsonResponse({'error': 'No valid voters found.'})
# def recognize_face(request):
#   image_path1=os.path.join(BASE_DIR,"AI_model","ImagesAttendance","image_testing","adithya","adithya.jpeg")
#   image_path2=os.path.join(BASE_DIR,"AI_model","ImagesAttendance","image_testing","sanosh","sanosh.jpeg")
#   image_path3=os.path.join(BASE_DIR,"AI_model","ImagesAttendance","image_testing","arjun","arjun.jpeg")
#   ema_img=face_recognition.load_image_file(image_path1)
#   ema_encoding=face_recognition.face_encodings(ema_img)[0]

#   bezos_img=face_recognition.load_image_file(image_path2)
#   bezos_encoding=face_recognition.face_encodings(bezos_img)[0]

#   arjun_img=face_recognition.load_image_file(image_path3)
#   arjun_encoding=face_recognition.face_encodings(arjun_img)[0]
#   known_face_encoding=[
#     ema_encoding,bezos_encoding,arjun_encoding
#   ]

#   known_face_names=[
#     "Adithya","sanosh","Arjun"
#   ]
#   clf=svm.SVC()
#   clf.fit(known_face_encoding,known_face_names)
#   valid_voters=known_face_names.copy()

#   face_locations = []
#   face_encodings = []
#   face_names = []
#   s =True
#   image_path=os.path.join(MEDIA_ROOT,"covers","image.jpeg")
#   frame=cv2.imread(image_path)
#   small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
#   rgb_small_frame = small_frame[:,:,::-1]
#   name=[]
#   if s:
#       face_locations=face_recognition.face_locations(small_frame)
#       face_encodings=face_recognition.face_encodings(small_frame,face_locations)
#       face_names=[]
#       for face_encoding in face_encodings:
#         name = clf.predict([face_encoding])
#         print(name)
#   return JsonResponse({'voter_name': name[0]})
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
@csrf_exempt
def submit_vote(request):
    decoded_body = request.body.decode('utf-8')

# Parse the JSON string
    data = json.loads(decoded_body)

# Extract the values
    candidate_id = data["candidate_id"]
    election_id = data["election_id"]
    print(request.body)
    print(candidate_id,type(candidate_id))
    candidate = get_object_or_404(Candidate, id=candidate_id)
    candidate.vote_count+=1
    candidate.save()
    return HttpResponse("vote submited")

class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()

class ElectionViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset=Election.objects.all()
    serializer_class=ElectionSerializer

class UserViewset(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class CandidateViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer

class VoteViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset=Vote.objects.all()
    serializer_class=VoteSerializer
    
class ImagerecViewset(viewsets.ModelViewSet):
    queryset=Imagerec.objects.all()
    serializer_class=ImagerecSerializer

class UserDetailViewset(viewsets.GenericViewSet,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
    serializer_class=UserDetailSerializer
    queryset=UserDetail.objects.all()    
    
    def post(self,request,*args,**kwargs):
        cover=request.data['cover']
        title=request.data['title']
        Imagerec.objects.create(title=title,cover=cover)
        return HttpResponse({'message': 'image created'},status=200)

class BlacklistTokenView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data["refresh_token"]
            token=RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LoggedInUserView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)