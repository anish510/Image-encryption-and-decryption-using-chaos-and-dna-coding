'''STEP 1'''

import cv2 as cv
#from PIL import Image
import numpy as np

# def get_image(v):
#     image=cv.imread(v)
#     #print(image)
#     '''to display image from 'image' matrix'''
#     # cv.imshow('image',image)
#     # cv.waitKey(0)
#     return image

def split_into_rgb_channels(pth): #openCV uses BGR format
   image=cv.imread(pth)
#    image=get_image(pth)
   red = image[:,:,2]
   green = image[:,:,1]
   blue = image[:,:,0]
   return red, green, blue

# r,g,b=split_into_rgb_channels(image)
# print('red channel :\n',r)
# print('green channel :\n',g)
# print('blue channel :\n',b)

# v=r'C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\female.tiff'
# r,g,b=split_into_rgb_channels(v)
# print('red channel :\n',r)
# print('green channel :\n',g)
# print('blue channel :\n',b)