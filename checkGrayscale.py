import cv2 as cv
import numpy as np

def check_grayscale(img_path):
    # Load the image
    img = cv.imread(img_path)

    # Loop through each pixel of the image
    for i in range(img.shape[0]): 
        for j in range(img.shape[1]):
            # Check if the values of the R, G, and B channels are the same
            if not (img[i, j, 0] == img[i, j, 1] == img[i, j, 2]):
                return 0

    return 1

# x=check_grayscale(r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\medical images\encrypted_images\encrypted_0026720152f5.png")
# print(x)