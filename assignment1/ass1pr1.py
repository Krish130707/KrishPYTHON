# (a) List of integers from 0 through 49
list_a = [i for i in range(50)]

# (b) Squares of integers from 1 through 50
list_b = [i**2 for i in range(1, 51)]

# (c) ['a','bb','ccc',...,'zz...z' (26 times)]
list_c = [chr(97+i) * (i+1) for i in range(26)]

print(list_a)
print(list_b)
print(list_c)
