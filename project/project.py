import math

def dot_product(vector_a, vector_b):
    return sum(a*b for a, b in zip(vector_a, vector_b))

def cross_product(vector_a, vector_b):
    x = vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1]
    y = vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2]
    z = vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
    return (x, y, z)

def angle_between(vector_a, vector_b, in_radians=False):
    dot = dot_product(vector_a, vector_b)
    magnitude_a = magnitude(vector_a)
    magnitude_b = magnitude(vector_b)
    cos_angle = dot / (magnitude_a * magnitude_b)
    angle = math.acos(cos_angle)
    if in_radians:
        return angle
    return math.degrees(angle)

def magnitude(vector):
    return math.sqrt(sum(coordinate ** 2 for coordinate in vector))

def add_vectors(vector_a, vector_b):
    return tuple(a+b for a, b in zip(vector_a, vector_b))

def subtract_vectors(vector_a, vector_b):
    return tuple(a-b for a, b in zip(vector_a, vector_b))

def scalar_multiplication(vector, scalar):
    return tuple(scalar * a for a in vector)

def vector_projection(vector_a, vector_b):
    dot_ab = dot_product(vector_a, vector_b)
    magnitude_b_squared = dot_product(vector_b, vector_b)
    scalar_projection = dot_ab / magnitude_b_squared
    return scalar_multiplication(vector_b, scalar_projection)

def is_orthogonal(vector_a, vector_b):
    return dot_product(vector_a, vector_b) == 0

def unit_vector(vector):
    return scalar_multiplication(vector, 1/magnitude(vector))

def area_of_parallelogram(vector_a, vector_b):
    return magnitude(cross_product(vector_a, vector_b))

def volume_of_parallelepiped(vector_a, vector_b, vector_c):
    return abs(dot_product(vector_a, cross_product(vector_b, vector_c)))

import math


def perform_operations(operations, vector_a, vector_b=None, vector_c=None, scalar=None):
    results = []
    if "1" in operations:
        results.append(("Dot Product", dot_product(vector_a, vector_b)))
    if "2" in operations:
        results.append(("Cross Product", cross_product(vector_a, vector_b)))
    if "3" in operations:
        results.append(("Angle (in degrees)", angle_between(vector_a, vector_b)))
    if "4" in operations:
        results.append(("Magnitude", magnitude(vector_a)))
    if "5" in operations:
        results.append(("Vector Addition", add_vectors(vector_a, vector_b)))
    if "6" in operations:
        results.append(("Vector Subtraction", subtract_vectors(vector_a, vector_b)))
    if "7" in operations:
        results.append(("Scalar Multiplication", scalar_multiplication(vector_a, scalar)))
    if "8" in operations:
        results.append(("Vector Projection", vector_projection(vector_a, vector_b)))
    if "9" in operations:
        results.append(("Orthogonal", is_orthogonal(vector_a, vector_b)))
    if "10" in operations:
        results.append(("Unit Vector", unit_vector(vector_a)))
    if "11" in operations:
        results.append(("Area of Parallelogram", area_of_parallelogram(vector_a, vector_b)))
    if "12" in operations:
        results.append(("Volume of Parallelepiped", volume_of_parallelepiped(vector_a, vector_b, vector_c)))
    return results

def main():
    while True:
        print("\nVector Mathematics Toolkit")
        print("Enter the numbers of the operations you want to perform, separated by commas.")
        print("1. Dot Product")
        print("2. Cross Product")
        print("3. Angle Between Vectors")
        print("4. Magnitude of a Vector")
        print("5. Add Vectors")
        print("6. Subtract Vectors")
        print("7. Scalar Multiplication")
        print("8. Vector Projection")
        print("9. Check Orthogonality")
        print("10. Unit Vector")
        print("11. Area of Parallelogram")
        print("12. Volume of Parallelepiped")
        print("0. Exit")
        operations_input = input("Choose operations (e.g., 1,4,7): ")
        operations = operations_input.split(',')

        if "0" in operations:
            break

        vector_a = tuple(map(float, input("Enter the first vector (x, y, z): ").split(',')))
        vector_b = vector_c = None
        scalar = None

        if any(op in ["1", "2", "3", "5", "6", "8", "9", "11", "12"] for op in operations):
            vector_b = tuple(map(float, input("Enter the second vector (x, y, z): ").split(',')))
        if "12" in operations:
            vector_c = tuple(map(float, input("Enter the third vector (x, y, z): ").split(',')))
        if "7" in operations:
            scalar = float(input("Enter a scalar value: "))

        results = perform_operations(operations, vector_a, vector_b, vector_c, scalar)
        for name, result in results:
            print(f"{name}: {result}")

if __name__ == "__main__":
    main()
