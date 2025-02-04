students = []
for i in range(10):
    name = input(f"Enter name of student {i+1}: ").strip()[:15]
    students.append(name)

print("\nReversed Student Names:")
for name in students:
    print(name[::-1])  
