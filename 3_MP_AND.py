n = int(input("enter the number of nueron : "))

theta=1
x1=[]
x2=[]
yin1=[]
yop1=[]

for i in range(0,n):
    n1 = int(input("enter x1 : "))
    x1.append(n1)
    n2 = int(input("enter x2 : "))
    x2.append(n2)
#___w1=1 N w2=1_____________________________________________
w1=1
w2=1
print("w1=w2=1")

for i in range(0,n):
    yin = x1[i]*w1+x2[i]*w2
    yin1.append(yin)
    # theta=n*w-p
    theta=2*w-0
    if(yin>=theta):
        yop1.append(1)
    else:
        yop1.append(0)
# x1 x2 w1 w2 yin1 yop1
# 1  1  1  1   2    1
# 1  0  1  1   1    1
# 0  1  1  1   1    1
# 0  0  1  1   0    0
#__________________________________________________

print("x1 x2 w1 w2 yin1 yop1")
for i in range(0,n):
    print(x1[i]," ",x2[i]," ", w1," ", w2 ," ",yin1[i] ," ", yop1[i])


#___________________________________________________________
#___________________________________________________________
#___________________________________________________________
#___________________________________________________________
#___________________________________________________________



#___w1=1 N w2=-1_____________________________________________
yin2=[]
yop2=[]
w1=1
w2=-1
print("w1=1")
print("w2=-1")
for i in range(0,n):
    yin = x1[i]*w1+x2[i]*w2
    yin2.append(yin)
    if(yin>=theta):
        yop2.append(1)
    else:
        yop2.append(0)
# x1 x2 w1 w2 yin2 yop2
# 1  1  1  -1   2    1
# 1  0  1  -1   1    1
# 0  1  1  -1   1    1
# 0  0  1  -1   0    0
#__________________________________________________

print("x1 x2 w1 w2 yin2 yop2")
for i in range(0,n):
    print(x1[i]," ",x2[i]," ", w1," ", w2 ," ",yin2[i] ," ", yop2[i])

# OUTPUT
#enter the number of nueron : 4
#enter x1 : 1
#enter x2 : 1
#enter x1 : 1
#enter x2 : 0
#enter x1 : 0
#enter x2 : 1
#enter x1 : 0
#enter x2 : 0
#w1=w2=1
#x1 x2 w1 w2 yin1 yop1
#1   1   1   1   2   1
#1   0   1   1   1   1
#0   1   1   1   1   1
#0   0   1   1   0   0
#w1=1
#w2=-1
#x1 x2 w1 w2 yin2 yop2
#1   1   1   -1   0   0
#1   0   1   -1   1   1
#0   1   1   -1   -1   0
#0   0   1   -1   0   0
