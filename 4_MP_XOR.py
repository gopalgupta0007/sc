import pandas as pd 
import numpy as np 

print("Enter Weights") 
w11=int(input('Weights w11=')) 
w12=int(input('Weights w12=')) 
w21=int(input('Weights w21=')) 
w22=int(input('Weights w22=')) 
v1=int(input('Weights v1=')) 
v2=int(input('Weights v2=')) 
print('Enter threshold value') 

theta=1

x1=np.array([0,0,1,1])
x2=np.array([0,1,0,1])
z=np.array([0,1,1,0]) 
con=1 
y1=np.zeros((4,))
y2=np.zeros((4,))
y=np.zeros((4,)) 
zin1=np.zeros((4,))
zin2=np.zeros((4,)) 
while con==1: 
    zin1=x1*w11+x2*w12 
    zin2=x1*w21+x2*w22 
    for i in range(0,4): 
        if(zin1[i]>=theta):
            y1[i]=1
        else:
            y1[i]=0
        if(zin2[i]>=theta): 
            y2[i]=1
        else:
            y2[i]=0
    yin=np.array([]) 
    yin=y1*v1+y2*v2 
    for i in range(0,4):
        if(yin[i]>=theta): 
            y[i]=1
        else:
            y[i]=0 
    print("yin",yin) 
    print("Output of Net:") 
    y=y.astype(int) 
    print("y",y)
    print("z",z) 
    if(np.array_equal(y,z)):
        con=0 
    else:
        print("Net is not able to learn use another set of weigths and thresholds") 
        print("Enter Weights")
        w11=int(input('Weights w11=')) 
        w12=int(input('Weights w12=')) 
        w21=int(input('Weights w21=')) 
        w22=int(input('Weights w22=')) 
        v1=int(input('Weights v1=')) 
        v2=int(input('Weights v2=')) 
        theta=int(input('theta='))
print("MP Output:") 
print("Weights of neuron z1") 
print(w11)
print(w12)
print("Weights of neuron z2") 
print(w21)
print(w22)
print("Weights of neuron Y") 
print(v1)
print(v2) 
print("Threshold") 
print(theta)
