from asyncio.windows_events import NULL
import math


"""KEY GENERATION"""
#code to obtain SHA-256 hash
import hashlib
import string

# def generate_hash(f=0):
def generate_hash(a):
    # a=input('enter password: ')
    #a=input('passwrd')
    hashed=hashlib.sha256(a.encode('utf-8')).hexdigest() #this is string
    '''print("Hash value of '",a,"' is",hashed)'''
    #print(type(hashed))

    """k generator"""
    k1=hashed[:8]
    #print(k1)
    k2=hashed[8:16]
    #print(k2)
    k3=hashed[16:24]
    #print(k3)
    k4=hashed[24:32]
    #print(k4)
    k5=hashed[32:40]
    #print(k5)
    k6=hashed[40:48]
    #print(k6)
    k7=hashed[48:56]
    #print(k7)
    k8=hashed[56:]
    #print(k8)

    """dj generator"""

    #hextod
    d_1=int(k1, 16)
    d_2=int(k2, 16)
    d_3=int(k3, 16)
    d_4=int(k4, 16)
    d_5=int(k5, 16)
    d_6=int(k6, 16)
    d_7=int(k7, 16)
    d_8=int(k8, 16)
    #print("d_1",d_1)

    #dj calculator
    divsr=2**10
    d1=d_1/divsr
    d2=d_2/divsr
    d3=d_3/divsr
    d4=d_4/divsr
    d5=d_5/divsr
    d6=d_6/divsr
    d7=d_7/divsr
    d8=d_8/divsr
    
    return d1,d2,d3,d4,d5,d6,d7,d8
    #print('d1',d1)

#sign function
def fn_sign(x):
    if(x==0):
        return 0
    elif(x<0):
        return -1
    else:
        return 1

"""First set of TD-ERCS initial values"""
def firstSecondSet(password):
    d1,d2,d3,d4,d5,d6,d7,d8 = generate_hash(password)
    x0_f=(fn_sign(d1-d2)*d1) % 1
    mu_f=d2 %1
    alpha_f=d3 % math.pi
    m_f=d4 % 10
    # x0_s= (fn_sign(d5-d6)*d5) % 1
    x0_s= (fn_sign(d1-d2)*d5) % 1
    mu_s= d6 % 1
    alpha_s=d7 % math.pi
    m_s=d8 % 10
    return x0_f, mu_f, alpha_f, math.ceil(m_f), x0_s, mu_s, alpha_s, math.ceil(m_s)   #ceil is used because some of the password yielded m=0.something
    

# a,b,c,d=first_set()
# print('First Set')
# print('x0: ' ,a,'mu: ', b,'alpha: ', c,'m: ',d)
# print('')
# a,b,c,d=second_set()
# print('Second Set')
# print('x0: ' ,a,'mu: ', b,'alpha: ', c,'m: ',d)