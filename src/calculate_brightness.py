# imports
import sys
import os
from PIL import Image

# function that calculates the brightness of an image
def calculate(image):
    
    # translating a color image to black and white
    greyscale_image = image.convert('L')
    
    # histogram for that image
    histogram = greyscale_image.histogram()
    
    # find the sum of all the values in the histogram
    pixels = sum(histogram)
    
    # store the scale of values that the image takes
    brightness = scale = len(histogram)
    
    # iterate over the range of values
    for index in range(0, scale):
        
        # compute the ratio using the value of histogram at that index and pixels
        ratio = histogram[index] / pixels
        
        # finally calculate the brightness of the image
        brightness += ratio * (-scale + index)

    # return the brightness accordingly    
    return 1 if brightness == 255 else round((brightness / scale)*10)