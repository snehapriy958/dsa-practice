"""
Problem: Third Maximum Number
Platform: LeetCode (414)
Difficulty: Easy
Approach: Set for Uniqueness + Sorting
Time Complexity: O(n log n) due to sorting (or O(n) if using three variables)
Space Complexity: O(n) to store unique elements
"""

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        return sorted(nums)[-3]