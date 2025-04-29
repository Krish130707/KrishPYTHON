import random

binary_list = [random.randint(0, 1) for _ in range(100)]

max_run = 0
current_run = 0
for bit in binary_list:
    if bit == 0:
        current_run += 1
        max_run = max(max_run, current_run)
    else:
        current_run = 0

print("Random Binary List:", binary_list)
print("Longest run of zeros:", max_run)
