def check_validity(equivalence_classes,n):

    is_Universal = set()

    for classes in equivalence_classes.values():
        is_Universal.update(classes)

    return is_Universal == set(range(1, n+1))

equivalence_classes = {0: [], 1: [], 2: [], 3: [], 4: []}

for num in range(1, 10000+1):
        remainder = num % 5
        equivalence_classes[remainder].append(num)
#print(equivalence_classes[0])
valid = check_validity(equivalence_classes, 10000)

if valid:
    print("equivalence classes of modulo 5 are valid")
else:
    print("equivalence classes modulo of 5 are not valid.")