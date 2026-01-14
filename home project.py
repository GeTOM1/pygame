n = int(input("Enter the size of the square matrix: "))

matrix = []

# Taking input
for i in range(n):
    row = []
    for j in range(n):
        value = int(input(f"Enter value for position [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

# Printing the matrix
print("\nSquare Matrix:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()