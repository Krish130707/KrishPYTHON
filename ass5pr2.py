class gfparty():
    def __init__(self,k):
        self.k=k
    def pieces(self):
        h=self.k//2
        v=self.k-h
        return h*v
num=int(input("enter the number of case : "))
for i in range (0,num):
    temp=int(input(f"{i+1}) enter the number : "))
    chocolatepieces=gfparty(temp)
    print(f"max no pieces for \"GF\" for {temp} cuts is {chocolatepieces.pieces()}")