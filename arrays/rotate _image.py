# Problem: Rotate Matrix
# Platform: LeetCode
# Difficulty: Medium
# Approach: Transpose + Reverse
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def rotate(matrix):
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:
        row.reverse()