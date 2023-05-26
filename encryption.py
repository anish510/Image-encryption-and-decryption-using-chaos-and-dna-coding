import numpy as np
import cv2 as cv
import os
import keygen_mod
import chaos_map as tdercs
import image_to_RGB_Matrices_mod as imgsplit
import DNAEncoding as dna_code
import checkGrayscale as chkGrays


def encryption(img_pth,passwd):

    '''Key Generation from User Password'''
    x0_f,mu_f,alph_f,m_f,x0_s,mu_s,alph_s,m_s=keygen_mod.firstSecondSet(passwd)



    '''Step 1'''
    #image split_into_rgb_channels
    # img_pth=r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\female_from_fb.jpg"
    r,g,b=imgsplit.split_into_rgb_channels(img_pth)
    t1=chkGrays.check_grayscale(img_pth)
    rows,colmns=r.shape
    # print(r)



    '''Step 2'''
    #chotic sequence for confusion
    #first set
    # x_new,trash_1,trash_2=tdercs.generate_map(x0_f,mu_f,alph_f,m_f,rows)

    # trash_3,y_new,trash_4=tdercs.generate_map(x0_f,mu_f,alph_f,m_f,colmns)
    x_new,y_new,trash_1=tdercs.generate_map(x0_f,mu_f,alph_f,m_f,rows,colmns)



    '''Step 3'''
    x_sort=sorted(x_new)
    y_sort=sorted(y_new)

    x_record=[]
    y_record=[]

    for i in range(len(x_sort)):
        for j in range(len(x_new)):
            if x_sort[i]==x_new[j]:
                x_record.append(j)

    for k in range(len(y_sort)):
        for l in range(len(y_new)):
            if y_sort[k]==y_new[l]:
                y_record.append(l)



    '''Step 4'''
    R_new=np.zeros_like(r)
    G_new=np.zeros_like(r)
    B_new=np.zeros_like(r)

    for m_ in range(rows):
        for n_ in range(colmns):
            R_new[m_,n_]=r[x_record[m_],y_record[n_]]
            G_new[m_,n_]=g[x_record[m_],y_record[n_]]
            B_new[m_,n_]=b[x_record[m_],y_record[n_]]

    '''uncomment this to view shuffled image'''
    # # print(R_new,G_new,B_new)
    # diffused=np.dstack((B_new,G_new,R_new))
    # print(diffused.ndim)
    # cv.imshow('diffused',diffused)
    # cv.imwrite(r'C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\shuff.tiff',diffused)
    # cv.waitKey(0)



    '''Step 5'''
    #DNA coding
    Bdna,Gdna,Rdna=dna_code.dna_encode(B_new,G_new,R_new)



    '''Step 6'''
    seq_len=rows*colmns
    Xn,Yn,Zn=tdercs.generate_map(x0_s,mu_s,alph_s,m_s,seq_len,seq_len)
    #print(Xn,Yn,Zn)

    Xe=[None]*seq_len
    Ye=[None]*seq_len
    Ze=[None]*seq_len
    for i in range(seq_len):
        Xe[i]=round((abs(Xn[i])*1000) % 256)
        Ye[i]=round((abs(Yn[i])*500) % 256)
        Ze[i]=round((abs(Zn[i])*1000) % 256)



    '''Step 7'''
    #converting Xe,Ye,Ze to 1D numpy arrays
    # Xe_in=np.array(Xe,dtype='uint8')
    # Ye_in=np.array(Ye,dtype='uint8')
    # Ze_in=np.array(Ze,dtype='uint8')
    Xe_in = np.clip(Xe, 0, 255).astype('uint8')
    Ye_in = np.clip(Ye, 0, 255).astype('uint8')
    Ze_in = np.clip(Ze, 0, 255).astype('uint8')


    #converting Xe,Ye,Ze to 2D matrix
    X_e=np.reshape(Xe_in,(rows,colmns))
    Y_e=np.reshape(Ye_in,(rows,colmns))
    Z_e=np.reshape(Ze_in,(rows,colmns))

    if not t1:
        Xdna,Ydna,Zdna=dna_code.dna_encode(X_e,Y_e,Z_e) #for color image
    else:
        Xdna,Ydna,Zdna=dna_code.dna_encode(X_e,X_e,X_e) #for gray image



    '''Step 8'''
    Bc,Gc,Rc=dna_code.xor_operation_new(Bdna,Gdna,Rdna,Xdna,Ydna,Zdna)

    Benc,Genc,Renc=dna_code.dna_decode(Bc,Gc,Rc)

    encrypted=np.dstack((Benc,Genc,Renc))
    # cv.imshow('Encrypted Image',encrypted) #uncomment to show encrypted image
    # cv.waitKey(0)



    # '''ALWAYS make the encrypted image file format lossless'''
    # cv.imwrite(r'C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\medical images\05a70a1c16c1-Ram2040-02-28.png',encrypted)
    output_dir = os.path.join(os.path.dirname(img_pth), "encrypted_images") #added later
    os.makedirs(output_dir, exist_ok=True) #added later
    file_name=os.path.basename(img_pth)
    encrypted_file_name = "encrypted_" + os.path.splitext(file_name)[0] + ".png"
    # encrypted_file_path = os.path.join(os.path.dirname(img_pth), encrypted_file_name)
    encrypted_file_path = os.path.join(output_dir, encrypted_file_name)

    if t1:
        gray_img = cv.cvtColor(encrypted, cv.COLOR_BGR2GRAY)
        # cv.imwrite(r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\female-mno.png",gray_img)
        cv.imwrite(encrypted_file_path,gray_img)
    else:
        # cv.imwrite(r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\female-mno.png", encrypted)
        cv.imwrite(encrypted_file_path,encrypted)

    return encrypted_file_path