'''
Problem: 3043. Longest Common Prefix of Two Arrays
Level: Medium
Platform: LeetCode
Approach: 1. Create a set to store all prefixes of numbers in the first array.
          2. For each number in the second array, check its prefixes against the set and keep track of the longest common prefix found. 
Time Complexity: O(n * m) where n is the length of arr1 and m is the length of arr2, due to the prefix generation and checking.
Space Complexity: O(n * k) where n is the length of arr1 and k is the average number of prefixes per number, due to the storage of prefixes in the set.
'''


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes = set()
        
        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10
        
        max_length = 0
        for val in arr2:
            while val > 0:
                if val in prefixes:
                    max_length = max(max_length, len(str(val)))
                    break 
                val //= 10
                
        return max_length