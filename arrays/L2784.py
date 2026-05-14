'''
problem : 2784. Check if Array is Good
platform : LeetCode (2784)
difficulty : easy
approach : sorting
time complexity : O(n log n) where n is the length of nums
space complexity : O(1) if we ignore the space used for sorting, otherwise O(n) for the sorted array

'''

from aiohttp_retry import List
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)

        x=list(range(1,n))
        x.append(n-1)
        return nums==x