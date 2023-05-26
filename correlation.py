#correlation
import cv2 as cv
import math
import matplotlib.pyplot as plt

def correlation(imgg):
    h=imgg.shape[1]
    # h=img.shape[0]
    N=h
    r1=10
    r2=11
    # c1=10
    # c2=11
    _ex=0
    _ey=0
    _dx=0
    _dy=0
    Dx=0
    Dy=0
    cov=0

    for i in range(h):
        _ex+=imgg[r1][i]
    Ex=_ex/N

    for i in range(h):
        _ey+=imgg[r2][i]
    Ey=_ey/N

    for i in range(h):
        # print(img[i][c1])
        _dx+=pow(imgg[r1][i]-Ex,2)
    Dx=_dx/N
    #print(Dx)

    for i in range(h):
        _dy+=pow(imgg[r2][i]-Ey,2)
    Dy=_dy/N
    #print(Dy)

    c=0
    a=0
    b=0

    for i in range(h):
        a=imgg[r1][i]-Ex
        b=imgg[r2][i]-Ey
        c+=a*b

    cov=c/N

    r_xy=(cov)/pow(Dx*Dy,0.5)
    print(r_xy)

img=cv.imread(r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\encrypted_images\encrypted_6.3.09.png")
# print(img[:,:,1])
correlation(img[:,:,2])
correlation(img[:,:,1])
correlation(img[:,:,0])