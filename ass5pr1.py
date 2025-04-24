class XOR:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def xor(self):
        maxi=0
        for i in range( self.a , self.b + 1):
            for j in range( i , self.b + 1):
                print(f"{i} XOR {j} = {i^j}")
                maxi=max(maxi,i^j)
        return maxi
NUM1=int(input("ENTER FIRST NUMBER (L) : "))
NUM2=int(input("ENTER SECOND NUMBER (R) : "))
ans=XOR(NUM1,NUM2)
print(f"THE MAXIMUM XOR VALUE OF ({NUM1},{NUM2}) IS {ans.xor()}")