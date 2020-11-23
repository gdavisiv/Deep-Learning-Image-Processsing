#import the packages
import numpy as np
import cv2
import os

class SimpleDatasetLoader:
    def __init__(self, preprocessors=None):
        #stores the image preprocessor
        self.preprocessors = preprocessors
        
        #