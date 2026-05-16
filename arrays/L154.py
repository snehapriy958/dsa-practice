'''
problem : 154. Find Minimum in Rotated Sorted Array II
platform : LeetCode (154)
difficulty : hard
approach : Binary Search
Time Complexity : O(log n) where n is the length of the input array in the average
case, but can degrade to O(n) in the worst case when there are many duplicates
Space Complexity : O(1) for the constant space used by the algorithm

'''
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1

        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            elif nums[mid]<nums[right]:
                right=mid
            else:
                right-=1
                
        return nums[left]
