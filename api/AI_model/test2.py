import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'media'))





#load image
ema_img=face_recognition.load_image_file('./sample_images/ema.jpeg')
ema_encoding=face_recognition.face_encodings(ema_img)[0]

bezos_img=face_recognition.load_image_file('./sample_images/jeffbezos.jpg')
bezos_encoding=face_recognition.face_encodings(bezos_img)[0]

kristen_img=face_recognition.load_image_file('./sample_images/kristen.jpeg')
kristen_encoding=face_recognition.face_encodings(kristen_img)[0]

# elon_img=face_recognition.load_image_file('./sample_images/')
hari_img=face_recognition.load_image_file('./sample_images/hari.jpeg')
hari_encoding=face_recognition.face_encodings(hari_img)[0]

nandu_img=face_recognition.load_image_file('./sample_images/nandv.jpeg')
nandu_encoding=face_recognition.face_encodings(nandu_img)[0]

alen_img=face_recognition.load_image_file('./sample_images/alen.jpeg')
alen_encoding=face_recognition.face_encodings(alen_img)[0]

known_face_encoding=[
    ema_encoding,bezos_encoding,kristen_encoding,hari_encoding,nandu_encoding,alen_encoding
]

known_face_names=[
    "Ema watson","Jeff Bezos","Kristen Stewart","Hari Kri","Nandu B","Alen"
]

valid_voters=known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s=True

now=datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+'.csv','w+',newline = '')
cswriter=csv.writer(f)

image_path=os.path.join(MEDIA_ROOT,"covers","hi","aaamm.jpg")
frame=cv2.imread(image_path)
small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
rgb_small_frame = small_frame[:,:,::-1]
if s:
    face_locations=face_recognition.face_locations(small_frame)
    face_encodings=face_recognition.face_encodings(small_frame,face_locations)
    face_names=[]

    for face_encoding in face_encodings:
        matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
        face_distance=face_recognition.face_distance(known_face_encoding,face_encoding)
        best_index=np.argmin(face_distance)
        name=""
        if matches[best_index]:
            name=known_face_names[best_index]
        face_names.append(name)

        if name in known_face_names:
            if name in valid_voters:
                valid_voters.remove(name)
                print(valid_voters)
                current_time=now.strftime("%H-%M-%S")
                cswriter.writerow([name,current_time])


    
 

f.close()
print("c0de completed")
