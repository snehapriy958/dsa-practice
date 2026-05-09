# Problem: Cyclically Rotating a GridPlatform: 
# LeetCode (1914)
# Difficulty: Medium
# Approach: Layer-by-Layer Simulation with Modulo Optimization
# Time Complexity: O(m * n)
# Space Complexity: O(m + n)

from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        top, left, bottom, right = 0, 0, m - 1, n - 1
        
        while top < bottom and left < right:
            # 1. Collect elements in counter-clockwise order
            layer = []
            for j in range(left, right): layer.append(grid[top][j])      # Top row
            for i in range(top, bottom): layer.append(grid[i][right])   # Right column
            for j in range(right, left, -1): layer.append(grid[bottom][j]) # Bottom row
            for i in range(bottom, top, -1): layer.append(grid[i][left])   # Left column
            
            # 2. Rotate using modulo to handle large k efficiently
            shift = k % len(layer)
            rotated = layer[shift:] + layer[:shift]
            
            # 3. Write rotated values back into the grid
            idx = 0
            for j in range(left, right):
                grid[top][j] = rotated[idx]; idx += 1
            for i in range(top, bottom):
                grid[i][right] = rotated[idx]; idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]; idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]; idx += 1
            
            # Move to the next inner layer
            top += 1; left += 1; bottom -= 1; right -= 1
            
        return grid
