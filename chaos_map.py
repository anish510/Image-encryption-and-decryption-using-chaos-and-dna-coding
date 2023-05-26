import math

def generate_map(x0,mu,alpha,m,rows,colmns):
#parameters from the hash are the first 4 arguments
#the last two the size of the image

    # n=iter

    if (rows>=colmns):
        n=rows
    else:
        n=colmns
    
    #define arrays of length i+1
    x=[None]*(n) #(i*j+1)
    y=[None]*(n) #(i*j+1)
    #kd=[None]*(n+1)
    k=[None]*(n)

    #initialize the first values of the array
    x[0]=x0
    y[0]=mu * math.sqrt(1 -math.pow(( x[0 ]),2)) 
    kd0=-( x[0]/ y[0] ) * math.pow(mu,2)
    k[0]=-((math.tan(alpha)+kd0)/(1-kd0*math.tan(alpha)))

    #loop to calculate other values of x and y
    for n in range(1,n):
        #for k'n-m
        if n<m:
            kd=-(x[n-1]/y[n-1])*math.pow(mu,2)
        else:
            kd=-(x[n-m]/y[n-m])*math.pow(mu,2)
        #for kn
        k[n]=(2*kd-k[n-1]+k[n-1]*math.pow(kd,2))/(1+(2*k[n-1]*kd)-math.pow(kd,2))
        #for xn
        x[n]=-(2*k[n-1]*y[n-1]+x[n-1]*(math.pow(mu,2)-math.pow(k[n-1],2)))/(math.pow(mu,2)+math.pow(k[n-1],2))
        #for yn
        y[n]=k[n-1]*(x[n]-x[n-1]) + y[n-1]
    
    return x[:rows],y[:colmns],k

'''function test'''
# #x0:  0.21875 mu:  0.23828125 alpha:  1.2995242990056965 m:  8, image size:3X4
# b,n,v=generate_map(0.21875,0.23828125,1.2995242990056965,8,1024)
# #print(v,'\n',b,'\n',n,'\n')
# print(v)

# #checking uniqueness
# flag=0
# for i in range(len(v)):
#     for j in range(len(v)):
#         if i!=j: 
#             if v[i]==v[j]:
#                 flag=1
#     if flag==1:
#         print('the elements are not unique')
#         break
# if flag==0:
#     print('the elements are unique')