classes = {i: [] for i in range(5)}
for num in range(1, 10001):
    classes[num % 5].append(num)

# Validity check
all_elements = []
for values in classes.values():
    all_elements.extend(values)

print("Are all elements covered exactly once:", sorted(all_elements) == list(range(1, 10001)))
print("Equivalence classes modulo 5:")
for key in classes:
    print(f"Class {key}: Sample -> {classes[key][:5]}")

