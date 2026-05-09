# Problem: Two Sum
# Platform: LeetCode (1)
# Difficulty: Easy
# Approach: Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return [d[target - n], i]
        d[n] = i