num=int(input("Enter the number to find digital root: "))
real_num=num


while num>9:
    sum=0
    while num!=0:
        rem=num%10
        sum+=rem
        num=num//10
    num=sum
print(num)
