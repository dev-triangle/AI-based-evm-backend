import cv2
import numpy as np
import os
#collecting daataset and assigning classes
cap = cv2.VideoCapture("0")
face_cascade = cv2.CascadeClassifier("C:\\Users\gagan\Desktop\haarcascade_frontalface_alt.xml")
skip = 0
face_data = []
labels = []
names = {}
class_id = 0
face_section = np.zeros((100,100),dtype="uint8")
dirpath = "C:\\Users\adithya\Desktop\data"
for file in os.listdir("C:\\Users\adithya\Desktop\data"):
    if file.endswith(".npy"):
        data_item = np.load(dirpath+'\\'+file)
        print(file)
        print("dataitem",data_item)
        names[class_id] = file[:-4]
        face_data.append(data_item)
        print("face_data",face_data)
        target = class_id * np.ones((data_item.shape[0],))
        class_id += 1
        labels.append(target)
face_dataset = np.concatenate(face_data,axis = 0)
print(f"facedataset {face_dataset} len= {len(face_dataset)}")
face_labels = np.concatenate(labels,axis = 0).reshape((-1,1))
