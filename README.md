## Directory structure

SIGNZY-TASK
    
    - images
        
        # contained images that were used to create the "train" directory, all of the images have now been moved to their respective target folders "train/<target_label>" using "create_dataset.py"
    
    - pickled_data
        
        # this file contains the features pickled for later use
        - X.pickle
        
        # this file contains the targets pickled for later use
        - y.pickle
    
    - src
        
        # this file calculates brightness_score of an image using Pillow
        - calculate_brightness.py
        
        # this file uses the images in the "images" folder and moves the image to appropriate folder by using the value returned by calculate_brightness i.e. creates the dataset by moving images to their respective target folder
        - create_dataset.py
        
        # this file creates the features and labels and saves it to "pickled_data"
        - create_training_data.py
        
        # this file uses the pickled data and creates a model on top of it
        - model.py
    
    - train
        
        # dataset the model was trained on
        - contains target folders containing data
    
    - model.json
        
        # the json file of the used model
    
    - model_weights.h5

        # saved model weights

    - model.h5

        # the saved model
    
    - README.md

    - test.jpg
        # test image in the "instructions to run" below

## Required libraries

- keras
- numpy
- Pillow
- opencv


## Instructions to Run

- navigate to src/
- run using
    >>> python predict.py
    >>> Please enter the filepath for the image to predict brightness: ../test.jpg
    >>> Predicted brightness_score : [7]

## Training a newer dataset

The execution process

- navigate to src/

1. execute create_dataset.py # this will store the images into respective target folders according to theier brightness scores(0-10) as calculated using calculate_brightness.py
2. execute create_training_data.py # this will create the features, target labels and save them to pickle inside /pickled_data
3. execute model.py # this will train the model if all of the directory structure is okay
4. execute predict.py as shown above

## Results - After training for 20 epochs

Training
    
    >>> loss: 0.1130 - acc: 0.9724

Validation

    >>> val_loss: 0.1990 - val_acc: 0.9457

## Due to time constraints, could not tweak the model parameters to achieve higher accuracy