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