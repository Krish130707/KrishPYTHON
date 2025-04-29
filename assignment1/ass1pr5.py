names = []
for _ in range(10):
    name = input("Enter a student name (max 15 characters): ")[:15]
    names.append(name)

reversed_names = [name[::-1] for name in names]
print("Reversed Names:")
for name in reversed_names:
    print(name)
