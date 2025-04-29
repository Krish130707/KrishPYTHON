def fibo(n):
    a=0
    b=1
    while a<n:
        temp=b
        b=a+b
        a=temp
    return a==n

n=int(input("enter number of testcases : "))
print(f"Enter {n} numbers")
numbers=[]
for i in range (0,n):
    k=int(input())
    numbers.append(k)
for j in range(0,n):
    if(fibo(numbers[i])):
        print("isfibo")
    else:
        print("isnotfibo")
