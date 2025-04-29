T=int(input("Enter number testcases : "))
print("Enter numbers as (x y)")
list2=[]
for i in range (0,T):
    user_input=input()
    numbers = list(map(int, user_input.split()))
    start=numbers[0]
    end=numbers[1]
    num=1
    count=0
    while num*num<start:
        num+=1

    while num*num<=end:
        num+=1
        count+=1
    list2.append(count)
for i in range (0,T):
    print(list2[i])

