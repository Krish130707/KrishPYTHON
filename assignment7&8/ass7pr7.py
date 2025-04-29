import math

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def rotation(self):
        return math.degrees(math.atan2(self.y, self.x))

    @staticmethod
    def distance(v1, v2):
        return math.sqrt((v2.x - v1.x) ** 2 + (v2.y - v1.y) ** 2)

    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y

    @staticmethod
    def cross_product(v1, v2):
        return v1.x * v2.y - v1.y * v2.x  # Returns a scalar for 2D

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Vector3D(Vector2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    @staticmethod
    def distance(v1, v2):
        return math.sqrt((v2.x - v1.x) ** 2 + (v2.y - v1.y) ** 2 + (v2.z - v1.z) ** 2)

    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross_product(v1, v2):
        return Vector3D(
            v1.y * v2.z - v1.z * v2.y,
            v1.z * v2.x - v1.x * v2.z,
            v1.x * v2.y - v1.y * v2.x
        )

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

if __name__ == "__main__":
    print("Enter coordinates for 2D Vector 1:")
    x1, y1 = map(float, input().split())
    v1 = Vector2D(x1, y1)

    print("Enter coordinates for 2D Vector 2:")
    x2, y2 = map(float, input().split())
    v2 = Vector2D(x2, y2)

    print(f"\nMagnitude of v1: {v1.magnitude()}")
    print(f"Rotation of v1: {v1.rotation()} degrees")
    print(f"Distance between v1 and v2: {Vector2D.distance(v1, v2)}")
    print(f"Dot product of v1 and v2: {Vector2D.dot_product(v1, v2)}")
    print(f"Cross product of v1 and v2: {Vector2D.cross_product(v1, v2)}")  # Correct for 2D

    print("\nEnter coordinates for 3D Vector 1:")
    x3, y3, z3 = map(float, input().split())
    v3 = Vector3D(x3, y3, z3)

    print("Enter coordinates for 3D Vector 2:")
    x4, y4, z4 = map(float, input().split())
    v4 = Vector3D(x4, y4, z4)

    print(f"\nMagnitude of v3: {v3.magnitude()}")
    print(f"Distance between v3 and v4: {Vector3D.distance(v3, v4)}")
    print(f"Dot product of v3 and v4: {Vector3D.dot_product(v3, v4)}")
    print(f"Cross product of v3 and v4: {Vector3D.cross_product(v3, v4)}")
