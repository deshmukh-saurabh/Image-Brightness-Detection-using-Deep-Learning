# imports
import calculate_brightness
import os
from PIL import Image

# the image directory(all the images from this directory will be moved to respective brightness_score(0-10) folders) in "../train/""
directory="../images/"

# to store all the calculated values
brightness_scores=[]

# to store all the filepaths
filepaths=[]

# iterate over the image directory and store all the file names in a list
files = [f for f in os.listdir(directory)]

# iterate over and print out the values
for file in files:
    
    # path to the file in consideration
    path=directory+file
    
    # add this to filepaths
    filepaths.append(path)
    
    # open the image using PIL.Image.open("<filepath>")
    image = Image.open(path)
    
    # round of the brightness to nearest integer
    brightness=calculate_brightness.calculate(image)
    
    # add this to scores
    brightness_scores.append(brightness)
    
    # move all the data from "images/" to "train/category" for ex. "train/1" for training
    new_path="../train/"+str(brightness)+"/"+file
    os.rename(path, new_path)

print("created training dataset in ../train/")
