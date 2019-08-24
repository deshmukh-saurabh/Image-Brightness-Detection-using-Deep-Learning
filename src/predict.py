# imports
from keras.models import load_model
import cv2
import numpy as np

# load the model
model = load_model('../model.h5')

model.compile(loss='binary_crossentropy',optimizer="adam",metrics=['accuracy'])

# image size
IMG_SIZE=50

# read in the filepath
filepath = input("Please enter the filepath for the image to predict brightness: ")

#read in the image
img_array=cv2.imread(filepath,cv2.IMREAD_GRAYSCALE)

# resize the image to be of size (IMG_SIZE,IMG_SIZE)
img_array=cv2.resize( img_array, (IMG_SIZE,IMG_SIZE) )

# reshape
img_array=np.array(img_array).reshape(-1,IMG_SIZE,IMG_SIZE,1)

# print the predicted brightness
print("Predicted brightness_score : ",model.predict_classes(img_array))