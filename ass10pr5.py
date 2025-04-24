'''5. The bisection method is a technique for finding solutions
(roots) to equations with a single unknown variable. Given
a polynomial function f, try to find an initial interval of f by
random probe. Store all the updates in an Numpy array.
Plot the root finding process using the matplotlib/pyplot library.'''

import numpy as np
import matplotlib.pyplot as plt
import random

def get_polynomial():
    poly_str = input("Enter a polynomial function in terms of x (e.g., 'x**3 - 2*x**2 + 4*x - 8'): ")

    def f(x):
        return eval(poly_str, {"__builtins__": None}, {"x": x})
        #eval() takes a string and executes it as Python code.
        #poly_str is the user-inputted polynomial function (e.g., "x**3 - 6*x**2 + 4*x + 12").
        #{"__builtins__": None} disables built-in functions for security.
        #{"x": x} creates a local variable x that is used in the evaluation of the polynomial.
        
    return f
        
def find_initial_interval(f):
    while True:
        a, b = sorted([random.uniform(-10, 10), random.uniform(-10, 10)])  # Random values in range
        if f(a) * f(b) < 0:  
            return a, b

def bisection_method(f, a, b, tol=1e-6):
    midpoints = []
    
    while abs(b - a) > tol: #abs = calculate absolute difference between b and a
        c = (a + b) / 2   # tol = tolerance level near about 0.000001(1e-6)
        midpoints.append(c) 
        
        if f(c) == 0:
            break 
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return np.array(midpoints) 

f = get_polynomial()
a, b = find_initial_interval(f)
print(f"Initial interval: [{a}, {b}]")

midpoints = bisection_method(f, a, b)

plt.plot(range(len(midpoints)), midpoints, marker='o', linestyle='-', color='b', label='Midpoints')
plt.axhline(y=midpoints[-1], color='r', linestyle='--', label=f'Estimated Root: {midpoints[-1]:.6f}')
plt.xlabel("Iteration")
plt.ylabel("Midpoint Value")
plt.title("Bisection Method Root Finding Process")
plt.legend()
plt.grid()
plt.show()
