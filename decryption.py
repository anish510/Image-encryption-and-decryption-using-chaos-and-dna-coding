import numpy as np
import cv2 as cv
import os
import keygen_mod
import chaos_map as tdercs
import image_to_RGB_Matrices_mod as imgsplit
import DNAEncoding as dna_code
import checkGrayscale as chkGrays


def decryption(img_pth,passwd):

    '''Key generation'''
    x0_f,mu_f,alph_f,m_f,x0_s,mu_s,alph_s,m_s=keygen_mod.firstSecondSet(passwd)



    '''Step 1'''
    #image to be decrypted is takenfrom:
    # img_pth=r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\female_from_fb-xyz.png"
    t1=chkGrays.check_grayscale(img_pth)
    r,g,b=imgsplit.split_into_rgb_channels(img_pth)
    rows,colmns= b.shape
    seq_len=rows*colmns



    '''Step 2'''
    Bdna,Gdna,Rdna=dna_code.dna_encode(b,g,r)
    #print(Bdna)



    '''Step 3'''
    Xi,Yi,Zi=tdercs.generate_map(x0_s,mu_s,alph_s,m_s,seq_len,seq_len)

    Xe=[None]*seq_len
    Ye=[None]*seq_len
    Ze=[None]*seq_len
    for i in range(seq_len):
        Xe[i]=round((abs(Xi[i])*1000) % 256)
        Ye[i]=round((abs(Yi[i])*500) % 256)
        Ze[i]=round((abs(Zi[i])*1000) % 256)

    # Xe_in=np.array(Xe,dtype='uint8')
    # Ye_in=np.array(Ye,dtype='uint8')
    # Ze_in=np.array(Ze,dtype='uint8')
    Xe_in = np.clip(Xe, 0, 255).astype('uint8')
    Ye_in = np.clip(Ye, 0, 255).astype('uint8')
    Ze_in = np.clip(Ze, 0, 255).astype('uint8')

    X_e=np.reshape(Xe_in,(rows,colmns))
    Y_e=np.reshape(Ye_in,(rows,colmns))
    Z_e=np.reshape(Ze_in,(rows,colmns))



    '''Step 4'''
    if not t1:
        Xdna,Ydna,Zdna=dna_code.dna_encode(X_e,Y_e,Z_e)
    else:
        Xdna,Ydna,Zdna=dna_code.dna_encode(X_e,X_e,X_e)



    '''Step 5'''
    Bd,Gd,Rd=dna_code.xor_operation_new(Bdna,Gdna,Rdna,Xdna,Ydna,Zdna)

    #decoding part
    Bdec,Gdec,Rdec=dna_code.dna_decode(Bd,Gd,Rd)



    '''Step 6'''
    # x_new,trash_1,trash_2=tdercs.generate_map(x0_f,mu_f,alph_f,m_f,rows)

    # trash_3,y_new,trash_4=tdercs.generate_map(x0_f,mu_f,alph_f,m_f,colmns)
    x_new,y_new,trash_1=tdercs.generate_map(x0_f,mu_f,alph_f,m_f,rows,colmns)


    '''Step 7'''

    x_sort=sorted(x_new)
    y_sort=sorted(y_new)

    x_rec=[]
    y_rec=[]
    for i in range(len(x_sort)):
        for j in range(len(x_new)):
            if x_sort[j]==x_new[i]:
                x_rec.append(j)

    unshuffled_image_r=np.empty_like((r))
    unshuffled_image_g=np.empty_like((g))
    unshuffled_image_b=np.empty_like((b))

    for k in range(len(y_sort)):
        for l in range(len(y_new)):
            if y_sort[l]==y_new[k]:
                y_rec.append(l)



    '''Step 8'''
    for m_ in range(rows):
        for n_ in range(colmns):
            unshuffled_image_r[m_,n_]=Rdec[x_rec[m_],y_rec[n_]]
            unshuffled_image_g[m_,n_]=Gdec[x_rec[m_],y_rec[n_]]
            unshuffled_image_b[m_,n_]=Bdec[x_rec[m_],y_rec[n_]]

    decrypted=np.dstack((unshuffled_image_b,unshuffled_image_g,unshuffled_image_r))
    #cv.imshow('Decrypted',decrypted) #uncomment to show decrypted image
    # cv.waitKey(0)

    file_name=os.path.basename(img_pth)
    decrypted_file_name = "decrypted_" + os.path.splitext(file_name)[0] + ".png"
    decrypted_file_path = os.path.join(os.path.dirname(img_pth), decrypted_file_name)

    if t1:
        gray_img = cv.cvtColor(decrypted, cv.COLOR_BGR2GRAY)
        # cv.imwrite(r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\female-mno.png",gray_img)
        cv.imwrite(decrypted_file_path, gray_img)
    else:
        # cv.imwrite(r"C:\Users\grish_ljqh0zt\Desktop\Major Project Work\image\female-mno.png", encrypted)
        cv.imwrite(decrypted_file_path, decrypted)

    return decrypted_file_path