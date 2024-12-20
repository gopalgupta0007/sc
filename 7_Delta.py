import numpy as np

x = np.zeros([3,]) 
weights = np.zeros([3,]) 
desired = np.zeros([3,]) 
actual = np.zeros([3,])

x,weights,desired,actual 
for i in range(0,3):
    x[i]=float(input("Enter Inputs :"))
print("Inputs are : ",x)

for i in range(0,3):
    weights[i]=float(input("Enter Initial weights :")) 
print("Weights are : ",weights)

for i in range(0,3):
    desired[i]=float(input("Enter Desired Output :")) 
print("Desired Output are :",desired)

a=float(input("Enter learning rate :")) 
print("Learning Rate is :",a)

actual= x*weights
print("Predicted Output is :",actual) 
print("Desired Output is :",desired)

while True:
    if np.array_equal(actual,desired): 
        break
    else:
        for i in range(0,3): 
            weights[i]=weights[i]+a*(desired[i]-actual[i])
    actual = x*weights

print("Final weights ",weights," makes predicted output ",actual," desired output ",desired ," same.")

