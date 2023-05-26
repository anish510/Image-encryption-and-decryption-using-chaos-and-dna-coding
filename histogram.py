import image_to_RGB_Matrices_mod as imgsplit
import cv2 as cv
import matplotlib.pyplot as plt

def inp_img(img_pth):
    r,g,b=imgsplit.split_into_rgb_channels(img_pth)
        
    hist_r = cv.calcHist([r], [0], None, [256], [-50, 300])
    hist_g = cv.calcHist([g], [0], None, [256], [-50, 300])
    hist_b = cv.calcHist([b], [0], None, [256], [-50, 300])

    # Plot the histograms
    plt.plot(hist_r, color='r')
    plt.show()
    plt.plot(hist_g, color='g')
    plt.show()
    plt.plot(hist_b, color='b')
    plt.show()
    
img_pth=r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\encrypted_images\encrypted_6.3.09.png"
inp_img(img_pth)