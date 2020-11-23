#import the necessary packages
import cv2

class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER.AREA):
        #stores the targe image width, height, and interpolation
        #this method is used when resizing
        self.width = width
        self.height = height
        self.inter = inter
        
    #The input image that we want to process    
    def preprocess(self, image):
        #resize the image to a fixed size, ignore the aspect ratio and return  to the calling function
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)