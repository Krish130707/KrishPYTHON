def count_to_make_palindrome(s):
    n=len(s)
    count=0
    for i in range (0,n//2):
        count+= abs(ord(s[i])-ord(s[n-i-1]))
    return count

T=int(input("Enter number testcases : "))
print("Enter strings")
string=[]
for i in range(0,T):
    s=input()
    string.append(s)
for i in range(0,T):
    k=count_to_make_palindrome(string[i])
    print(k)
