list1 = [1,2,3,4,5]
list2 = [6,7,8,9]

def overlapping(list1, list2):
    for i in range(0,len(list1)): 
        for j in range(0,len(list2)): 
            if(list1[i]==list2[j]):
                return 1
    
    return 0

if(overlapping(list1, list2)): 
    print("overlapping")
else:
    print("not overlapping") 



# NOT IN    
print("5 not in [2,3,4,6] => ",5 not in [2,3,4,6])



# IS
x = 5
if(type(x) is int): 
    print("True") 
else: 
    print("False")



# IS NOT 
x = 5.2
if(type(x) is not int): 
    print("True")
else: 
    print("False")
