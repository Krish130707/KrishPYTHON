feet=float(input("Enter a length in feet : "))
inches=float(12*feet)
yard=float(feet/3.0)
miles=float(feet/5280.0)
milimeter=float(feet*304.8)
list1=[feet,inches,yard,miles,milimeter]
list2=["feet","inches","yard","miles","milimeter"]

print("Enter 1 for inches")
print("Enter 2 for yard")
print("Enter 3 for miles")
print("Enter 4 for milimeter")
i=int(input("Enter a number : "))
print(f"The length in {list2[i]} is {list1[i]}") 