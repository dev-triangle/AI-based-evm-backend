import os
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Directory containing face images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

face_dir = os.path.join(BASE_DIR,'ImagesAttendance','image_training','aditjya')

# Create empty arrays for face data and labels
face_data = []
labels = []

# Loop through each file in the directory
for filename in os.listdir(face_dir):
    # Load the image and convert to grayscale
    img = cv2.imread(os.path.join(face_dir, filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Resize the image to 64x64 pixels
    resized = cv2.resize(gray, (64, 64))
    
    # Convert the image to a 3D array with 3 channels
    rgb = cv2.cvtColor(resized, cv2.COLOR_GRAY2RGB)
    
    # Add the image data to the face_data array
    face_data.append(rgb)
    
    # Add the label to the labels array
    labels.append(1) # replace with your label values
    
# Convert the face_data and labels arrays to NumPy arrays
face_data = np.array(face_data)
labels = np.array(labels)

# Save the face_data and labels arrays to files
np.save('face_data.npy', face_data)
np.save('labels.npy', labels)


# Load the face dataset
face_data = np.load('face_data.npy')
labels = np.load('labels.npy')

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(face_data, labels, test_size=0.2, random_state=0)

# Create the CNN model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Load an image for face recognition
image_path=os.path.join(BASE_DIR,'ImagesAttendance','image_testing','adithya','adithya.jpeg')
img = cv2.imread(image_path)
img = cv2.resize(img, (64, 64))

# Predict the label for the image
label = model.predict_step(np.array([img]))
if label == 1:
    print('This is a face!',labels[label])
else:
    print('This is not a face.')