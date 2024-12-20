numberOfNuron=int(input("enter numberOfNuron => "))
bias=float(input("enter bias => "))

x=[]
w=[]

for i in range(0,numberOfNuron):
    xVal = float(input("Enter the inputs : "))
    x.append(xVal)
    wVal = float(input("Enter the weight : "))
    w.append(wVal)

print("all inputs are => ", x)
print("all weights are => ", w)
print("bias are => ", bias)

yin=0.0
yin=yin+bias

for i in range(0,numberOfNuron):
    yin = yin + (w[i]*x[i])
print("yin=",yin)


# for binary activation function
thresh=float(input("enter thresh for binary => "))
if(yin>=thresh):
    print("binary input is 1")
else:
    print("binary input is 0")


# for bipolar activation function
thresh=float(input("enter thresh for bipolar => "))
if(yin>=thresh):
    print("binary input is 1")
else:
    print("binary input is -1")


# OUTPUT
#enter numberOfNuron => 3
#enter bias => 0.1
#Enter the inputs : 1
#Enter the weight : 0.1
#Enter the inputs : 2
#Enter the weight : 0.2
#Enter the inputs : 3
#Enter the weight : 0.3
#all inputs are =>  [1.0, 2.0, 3.0]
#all weights are =>  [0.1, 0.2, 0.3]
#bias are =>  0.1
#yin= 1.5
#enter thresh for binary => 1
#binary input is 1
#enter thresh for bipolar => 2
#binary input is -1
