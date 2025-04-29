word=input(("Enter any word : "))
length=len(word)
for i in range(length):
    if i%2==0:
        print(word[i],end='')
    else:
        s=word[i].capitalize()
        print(s,end='')