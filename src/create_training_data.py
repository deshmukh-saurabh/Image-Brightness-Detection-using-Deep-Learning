# imports
import numpy as np
import os
import cv2
import random
import pickle

# the training data directory
DATADIR="../train"

# the categories of brightness(brightness scores)
CATEGORIES=["0","1","2","3","4","5","6","7","8","9","10"]

# choose an image size
IMG_SIZE=50

# training set
training_data=[]

# function that will create our training set
def create_train_set():
    
    # iterate over all the categories
    for category in CATEGORIES:
        
        # path to each category
        path=DATADIR+"/"+category

        # the target class
        class_num=CATEGORIES.index(category)

        # iterate over all the images in the target class directory
        for image in os.listdir(path):
            
            try:
                
                #read in the image
                img_array=cv2.imread(path+"/"+image,cv2.IMREAD_GRAYSCALE)

                # resize the image to be of size (IMG_SIZE,IMG_SIZE)
                new_array=cv2.resize( img_array, (IMG_SIZE,IMG_SIZE) )

                # append this to training_data - [image_array,target_class]
                training_data.append([new_array,class_num])

            except Exception as e:
                pass

# create the train_set
create_train_set()

# print the len of our training set
print(f"length of training set = {len(training_data)}")

# shuffle the data
random.shuffle(training_data)

# create features and targets
X=[]
y=[]

# iterate over all the (feature,label) pairs and add them to respective sets
for feature,label in training_data:
    X.append(feature)
    y.append(label)

# reshape X
X=np.array(X).reshape(-1,IMG_SIZE,IMG_SIZE,1)

# save the created data
pickle_out=open("../pickled_data/X.pickle","wb")
pickle.dump(X,pickle_out)
pickle_out.close()

pickle_out=open("../pickled_data/y.pickle","wb")
pickle.dump(y,pickle_out)
pickle_out.close()

# completed creation of (feature,label) sets and saved pickles
print("Completed! pickles saved at ../pickled_data/")