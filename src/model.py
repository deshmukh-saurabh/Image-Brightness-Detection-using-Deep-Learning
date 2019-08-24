# imports
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils

# load the data from pickle
pickle_in=open("../pickled_data/X.pickle", "rb")
X=pickle.load(pickle_in)

pickle_in=open("../pickled_data/y.pickle", "rb")
y=pickle.load(pickle_in)

# scale data
X=X/255.0

# print the shape of our data
print('X shape:', X.shape)
print('y shape',len(y))

# constants
IMG_CHANNELS=1
IMG_ROWS=50
IMG_COLS=50
NB_CLASSES=11

y=np_utils.to_categorical(y,NB_CLASSES)

# create the model
model = Sequential()

# layer1 - input
model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=(IMG_ROWS, IMG_COLS, IMG_CHANNELS)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# layer2
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))

# layer3 - output
model.add(Dense(NB_CLASSES))
model.add(Activation('softmax'))

# print the model summary
print(model.summary())

# compile the model
model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["accuracy"])

# fit the model
model.fit(X,y, batch_size=32, validation_split=0.1,epochs=20)

#save model
model_json = model.to_json()
open('../model.json', 'w').write(model_json)
model.save("../model.h5")
model.save_weights('../model_weights.h5', overwrite=True)
