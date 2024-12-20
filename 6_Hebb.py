import numpy as np

x1 = np.array([1,1,1,-1,1,-1,1,1,1])
print(x1)

x2 = np.array([1,1,1,1,-1,1,1,1,1])
print(x2)
b = 0
y = np.array([1,-1])
wOld = np.zeros([9,]) 
print(wOld)

wNew = np.zeros([9,]) 
print(wNew)

wOld =wOld.astype(int) 
wNew =wNew.astype(int)

print(wOld, wNew)

print("For first pattern with target == 1") 
for i in range(0,9):
    wOld[i] = wOld[i] + x1[i]*y[0] 

wNew = wOld
b = b+y[0] 
print(wOld) 
print(b)

print("For second pattern with target == -1") 
for i in range(0,9):
    wNew[i] = wOld[i] + x2[i]*y[1] 
b = b+y[1]
print("New weights are ",wNew) 
print("Final bias is ",b)
