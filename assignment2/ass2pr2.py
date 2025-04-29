number = int(input("Enter the number of products :"))
dictionary = {}
for i in range (number):
    product_name = input("Enter the name of product :")
    price = int(input("Enter the price of the product :"))
    dictionary.update({product_name:price})

while(i):
    print("Enter -1 to exit")
    search = input("Enter the product :")
    if search in dictionary:
        print("Price :",dictionary[search])
    if search == '-1':
        exit(1)
    if not(search in dictionary):
        print("Product not found ")
    