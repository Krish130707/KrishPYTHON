'''Write a program to make the length of each element 15
of a given Numpy array and the string centered, left-justified, right-justified with paddings of _ (underscore)'''
import numpy as np

print("Enter Array Elemets separated by commas: ")
arr = np.array(input().split(','))

centered = np.char.center(arr, 15, '_')
left_justified = np.char.ljust(arr, 15, '_')
right_justified = np.char.rjust(arr, 15, '_')

print("Centered:")
print(centered)
print("\nLeft-Justified:")
print(left_justified)
print("\nRight-Justified:")
print(right_justified)

