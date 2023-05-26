import numpy as np
import cv2 as cv
import math

def mse_psnr(orig,encrypted):
    m,n,chnl=img1.shape
    sum=0
    for i in range(m):
        for j in range(n):
            for k in range(chnl):
                sum+=pow(int(img1[i,j,k])-int(img2[i,j,k]),2)
    mse=sum/(m*n*chnl)
    
    if mse:
        Imax=255
        psnr = 10 * np.log10(Imax**2 / mse)
        return (mse,psnr)
    else:
        return (mse,-1)


#not encrypted
img_pth1=r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\6.1.01.png"
img1=cv.imread(img_pth1)
#encrypted
img_pth2=r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\encrypted_images\decrypted_encrypted_6.1.01.png"
img2=cv.imread(img_pth2)

mse,psnr=mse_psnr(img1,img2)
print(mse,psnr)