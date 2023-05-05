from keras.preprocessing.image import ImageDataGenerator
import pickle
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dense
import numpy as np
import keras.utils as image
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TrainingImagePath = os.path.join(BASE_DIR, 'ImagesAttendance', 'image_training')
""" TrainingImagePath = './ImagesAttendance/image_training'
 """
train_datagen = ImageDataGenerator(
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True)

test_datagen = ImageDataGenerator()

training_set = train_datagen.flow_from_directory(
    TrainingImagePath,
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical')


test_set = test_datagen.flow_from_directory(
    TrainingImagePath,
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical')


print(test_set.class_indices)

TrainingClasses = training_set.class_indices
resultMap = {}
for facevalue, facename in zip(TrainingClasses.values(), TrainingClasses.keys()):
    resultMap[facevalue] = facename
print(resultMap)
with open("resultMap.pkl", "wb")as fileWriteStream:
    pickle.dump((resultMap), fileWriteStream)
outputneurons = len(resultMap)
print("the no of output neurons is ", outputneurons)
classifier = Sequential()
classifier.add(Convolution2D(32, kernel_size=(5, 5), strides=(
    1, 1), input_shape=(64, 64, 3), activation='relu'))

classifier.add(MaxPool2D(pool_size=(2, 2)))
classifier.add(Convolution2D(64, kernel_size=(
    5, 5), strides=(1, 1), activation='relu'))
classifier.add(MaxPool2D(pool_size=(2, 2)))
classifier.add(Flatten())
classifier.add(Dense(64, activation='relu'))
classifier.add(Dense(outputneurons, activation='softmax'))
classifier.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics=["accuracy"])
starttime = time.time()
classifier.fit(training_set,
               steps_per_epoch=len(training_set),
               epochs=10,
               validation_data=test_set,
               validation_steps=len(test_set))
entdtime=time.time()
print("####time take",round(entdtime-starttime)/60)
ImagePath=os.path.join(BASE_DIR,'ImagesAttendance','image_testing','adithya','adithya.jpeg')
""" ImagePath='ImagesAttendance/image_testing/adithya/adithya.jpeg'
 """
test_image=image.load_img(ImagePath,target_size=(64, 64))
print(test_image)
test_image=image.img_to_array(test_image)
 
test_image=np.expand_dims(test_image,axis=0)
 
result=classifier.predict(test_image,verbose=0)
#print(training_set.class_indices)
 
print('####'*10)
print('Prediction is: ',resultMap[np.argmax(result)])