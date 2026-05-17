'''
Problem: 1306. Jump Game III
Platform: LeetCode
Difficulty: Medium
Approach: Depth-First Search (DFS)
Time Complexity: O(n) where n is the length of the input array, as in the worst case we may visit each index once.
Space Complexity: O(n) in the worst case due to the recursion stack and the visited set

'''


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visited = set()
        
        def dfs(index):
            if index < 0 or index >= len(arr):
                return False

            if arr[index] == 0:
                return True

            if index in visited:
                return False
            
            visited.add(index)

            return dfs(index + arr[index]) or dfs(index - arr[index])
            
        return dfs(start)
