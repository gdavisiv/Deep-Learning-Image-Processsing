#import the packages
import numpy as np
import cv2
import os

class SimpleDatasetLoader:
    #This defines the constructor where we can pass in a list of image preprocessors , that can we sequentally
    #applied to a specific image that was inputted
    def __init__(self, preprocessors=None):
        #stores the image preprocessor
        self.preprocessors = preprocessors
        
        #if there is no preprocessors, initialize it as an empty list
        if self.preprocessors is None:
            self.preprocessors = []
            
        #This is our load method: needs a single paramater -> imagePaths, a list of 
        #file paths to images in our dataset this is stored on disk
        def load(self, imagePaths, verbose=-1):
            #Initialize the list of features and labels
            data = []
            labels = []
            
            #Loop over the input images
            for(i, imagePath) in enumerate(imagePaths):
                #load the image and extract the class label
                #assuming that the path follows this format ->
                #  /path/to/dataset/{class}/{image}.jpg
                image = cv2.imread(imagePath)
                label = imagePath.split(os.path.sep)[-2] 
                
                #check to see if preprocessors are not NONE
                if self.preprocessors is not None:
                    
                    for p in self.preprocessors:
                        image = p.preprocess(image)
                        
                data.append(image)
                labels.apprend(label)
                
                