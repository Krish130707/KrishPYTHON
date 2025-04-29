print("Initial height of utopian tree is 1 meter")
T=int(input("Entet number of testcases : "))
N=[]
print("Enter the number of cycle :")
for i in range (0,T):
    k=int(input())
    N.append(k)
for i in range (0,T):
    height=1
    for j in range(0,N[i]):
        if(j%2==0):
            height=height*2
        else:
            height=height+1
    print(height)
    



