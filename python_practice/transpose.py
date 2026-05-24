def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)
print("\nTransposed Matrix:")
for row in transposed:
    print(row)
    