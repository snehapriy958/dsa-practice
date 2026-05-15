'''
problem : 153. Find Minimum in Rotated Sorted Array
platform : LeetCode (153)
difficulty : medium
approach : Binary Search
Time Complexity : O(log n) where n is the length of the input array
Space Complexity : O(1) for the constant space used by the algorithm

'''

from aiohttp_retry import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]