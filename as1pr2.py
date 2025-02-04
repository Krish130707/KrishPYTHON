import random
list=[]
count=0
numof0=[]
for i in range(0,100):
    number=random.randint(0,1)
    list.append(number)
print("LIST :")
print(list)
for i in range(0,100):    
    if(list[i]==0):
        count+=1
    else:
        numof0.append(count)
        count=0
    
max_element=max(numof0)    
print("Longest run of 0 is :", max_element)