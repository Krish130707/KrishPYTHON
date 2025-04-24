str=input("Enter a sentence\n")
str=str.lower()
x=len(str)
pangram=set()
pangram={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
setofstr=set()
for i in range (0,x):
    if str[i].isalpha():
        setofstr.add(str[i])
if(setofstr==pangram):
    print("ispangram")
else:
    print("isnotpangram")
