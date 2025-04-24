'''A magic square is an N×N grid of numbers in which theentries in each row, column and main diagonal sum to the
same number (equal to N(N^2+1)/2). Create a magic squarefor N=4, 5, 6, 7, 8'''
import numpy as np

def generate_odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2
    
    for num in range(1, n * n + 1):
        magic_square[i, j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if magic_square[new_i, new_j]:
            i += 1
        else:
            i, j = new_i, new_j
    
    return magic_square

def generate_doubly_even_magic_square(n):
    """Generates a magic square for doubly even order (N % 4 == 0)."""
    magic_square = np.arange(1, n * n + 1).reshape(n, n)
    mask = np.zeros((n, n), dtype=bool)
    
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3):
                mask[i, j] = True
    
    magic_square[mask], magic_square[~mask] = magic_square[~mask], magic_square[mask]
    return magic_square

def generate_singly_even_magic_square(n):
    """Generates a magic square for singly even order (N % 4 == 2) using Strachey's method."""
    half_n = n // 2
    sub_square_size = half_n * half_n
    
    sub_square = generate_odd_magic_square(half_n)
    magic_square = np.zeros((n, n), dtype=int)
    
    for i in range(2):
        for j in range(2):
            magic_square[i * half_n:(i + 1) * half_n, j * half_n:(j + 1) * half_n] = sub_square + sub_square_size * (i * 2 + j)
    
    k = (n - 2) // 4
    for i in range(half_n):
        for j in range(k):
            magic_square[i, j], magic_square[i + half_n, j] = magic_square[i + half_n, j], magic_square[i, j]
        for j in range(n - k + 1, n):
            magic_square[i, j], magic_square[i + half_n, j] = magic_square[i + half_n, j], magic_square[i, j]
    
    magic_square[half_n, [0, k]] = magic_square[0, [0, k]]
    magic_square[0, [0, k]] = sub_square_size * 2 + np.array([1, 2])
    
    return magic_square

def generate_magic_square(n):
    """Wrapper function to generate magic squares for different values of N."""
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

def print_magic_square(square):
    """Prints the magic square in a readable format."""
    for row in square:
        print(" ".join(f"{num:2}" for num in row))
    print()

if __name__ == "__main__":
    for n in [4, 5, 6, 7, 8]:
        print(f"Magic Square for N={n}:")
        magic_square = generate_magic_square(n)
        print_magic_square(magic_square)
