import math

def distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

points = []
print("Enter 10 points in 3D (x y z):")
for _ in range(10):
    x, y, z = map(float, input().split())
    points.append((x, y, z))

nearest_neighbors = []

for i, p in enumerate(points):
    min_dist = float('inf')
    nearest = None
    for j, q in enumerate(points):
        if i != j:
            d = distance(p, q)
            if d < min_dist:
                min_dist = d
                nearest = q
    nearest_neighbors.append((p, nearest))

print("Point and its nearest neighbor:")
for pair in nearest_neighbors:
    print(f"{pair[0]} --> {pair[1]}")
