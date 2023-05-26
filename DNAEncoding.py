'''STEP 5'''
import numpy as np
#import image_to_RGB_Matrices_1 as im_to_rgb

# x=np.array([1,2,3,4])
# bin=np.vectorize(np.binary_repr)(x, 8)
# print(bin)

# #DNA-Encoding RULE #1 A = 00, T=01, G=10, C=11
# dna={}
# dna["00"]="A"
# dna["01"]="T"
# dna["10"]="G"
# dna["11"]="C"
# dna["A"]=[0,0]
# dna["T"]=[0,1]
# dna["G"]=[1,0]
# dna["C"]=[1,1]

#DNA-Encoding RULE #2 A = 00, T=11, G=10, C=01
dna={}
dna["00"]="A"
dna["11"]="T"
dna["10"]="G"
dna["01"]="C"
dna["A"]=[0,0]
dna["T"]=[1,1]
dna["G"]=[1,0]
dna["C"]=[0,1]

#DNA xor
dna["AA"]=dna["TT"]=dna["GG"]=dna["CC"]="A"
dna["AG"]=dna["GA"]=dna["TC"]=dna["CT"]="G"
dna["AC"]=dna["CA"]=dna["GT"]=dna["TG"]="C"
dna["AT"]=dna["TA"]=dna["CG"]=dna["GC"]="T"
#print(dna)


def dna_encode(b,g,r):
    
    b = np.unpackbits(b,axis=1)
    #print(b)
    g = np.unpackbits(g,axis=1)
    r = np.unpackbits(r,axis=1)
    m,n = b.shape
    #print(b.shape)
    r_enc= np.chararray((m,int(n/2)))
    #print('\n',r_enc)
    g_enc= np.chararray((m,int(n/2)))
    b_enc= np.chararray((m,int(n/2)))
    
    for color,enc in zip((b,g,r),(b_enc,g_enc,r_enc)):
        idx=0
        for j in range(0,m):
            for i in range(0,n,2):
                enc[j,idx]=dna["{0}{1}".format(color[j,i],color[j,i+1])]
                idx+=1
                if (i==n-2):
                    idx=0
                    break
    
    b_enc=b_enc.astype(str)
    g_enc=g_enc.astype(str)
    r_enc=r_enc.astype(str)
    return b_enc,g_enc,r_enc

#for function test
bl=np.array([[1,2],[3,0]],dtype='uint8')
gr=np.array([[1,2],[3,0]],dtype='uint8')
re=np.array([[1,2],[3,0]],dtype='uint8')
R_dna,G_dna,B_dna=dna_encode(bl,gr,re)
# print(a,'\n',b,'\n',c)

def dna_decode(b,g,r):
    m,n = b.shape
    r_dec= np.ndarray((m,int(n*2)),dtype=np.uint8)
    g_dec= np.ndarray((m,int(n*2)),dtype=np.uint8)
    b_dec= np.ndarray((m,int(n*2)),dtype=np.uint8)
    for color,dec in zip((b,g,r),(b_dec,g_dec,r_dec)):
        for j in range(0,m):
            for i in range(0,n):
                dec[j,2*i]=dna["{0}".format(color[j,i])][0]
                dec[j,2*i+1]=dna["{0}".format(color[j,i])][1]
    b_dec=(np.packbits(b_dec,axis=-1))
    g_dec=(np.packbits(g_dec,axis=-1))
    r_dec=(np.packbits(r_dec,axis=-1))
    return b_dec,g_dec,r_dec

# #for decoding function test
# q,w,e=dna_decode(R_dna,G_dna,B_dna)
# print(q,'\n',w,'\n',e)

def xor_operation_new(b,g,r,mk1,mk2,mk3):
    m,n = b.shape
    bx=np.chararray((m,n))
    gx=np.chararray((m,n))
    rx=np.chararray((m,n))
    b=b.astype(str)
    g=g.astype(str)
    r=r.astype(str)
    for i in range(0,m):
        for j in range (0,n):
            bx[i,j] = dna["{0}{1}".format(b[i,j],mk1[i,j])]
            gx[i,j] = dna["{0}{1}".format(g[i,j],mk2[i,j])]
            rx[i,j] = dna["{0}{1}".format(r[i,j],mk3[i,j])]
         
    bx=bx.astype(str)
    gx=gx.astype(str)
    rx=rx.astype(str)
    return bx,gx,rx 


'''this was used to check if the x-or's working properly'''
# def xor_operation(b,g,r):
#     m,n = b.shape
#     bx=np.chararray((m,n))
#     gx=np.chararray((m,n))
#     rx=np.chararray((m,n))
#     b=b.astype(str)
#     g=g.astype(str)
#     r=r.astype(str)
#     for i in range(0,m):
#         for j in range (0,n):
#             # bx[i,j] = dna["{0}{1}".format(b[i,j],mk[i,j])]
#             # gx[i,j] = dna["{0}{1}".format(g[i,j],mk[i,j])]
#             # rx[i,j] = dna["{0}{1}".format(r[i,j],mk[i,j])]
#             bx[i,j] = dna["{0}{}".format(b[i,j]),]
#             gx[i,j] = dna["{0}{}".format(g[i,j]),]
#             rx[i,j] = dna["{0}{}".format(r[i,j]),]
         
#     bx=bx.astype(str)
#     gx=gx.astype(str)
#     rx=rx.astype(str)
#     return bx,gx,rx