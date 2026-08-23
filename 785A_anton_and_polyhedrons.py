def solution():
    n = int(input())
    count = 0
    # Tetrahedron = 4 sides
    # Cube =6 sides
    # Octahedron= 8 sides
    # Dodecahedron = 12 sides
    # Icosahedron = 20 sides
    for i in range(n):
        shape = input().lower()
        if shape == "tetrahedron":
            count+=4
        elif shape == "cube":
            count+=6
        elif shape == "octahedron":
            count+=8
        elif shape == "dodecahedron":
            count+=12
        else:
            count+=20

    print(count)

solution()