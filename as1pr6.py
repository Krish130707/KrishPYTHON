import math 
def dis(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)
list = []
print("Enter 5 points (as x y z)")
for i in range(5):
    point = tuple(map(int,input(f"Enter point {i+1} : ").split()))
    list.append(point)
closest_point = []
for i in range(5):
    min_dist = float("inf")  # positive infinity to initialize first case
    curr_point = list[i]
    nearest = None
    for j in range(5):
        if(i!=j):
            dist = dis(curr_point,list[j])
            if(dist<min_dist):
                min_dist = dist
                nearest = list[j]
    closest_point.append((curr_point,nearest))

for point,neighbor in closest_point:
    print(f"{point} nearest to {neighbor}")