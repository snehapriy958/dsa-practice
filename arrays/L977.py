'''

Problem: Squares of a Sorted Array
Platform: LeetCode (977)
Difficulty: Easy
Approach: Map Squares + Sorting
Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) if we ignore the space used for sorting (or O(n) if we consider the output array)

'''


class Solution:
    def sortedSquares(self, nums: list) -> list:
        for index in range(len(nums)):
            nums[index] = nums[index] ** 2
        nums.sort()
        return nums
    
if __name__ == '__main__':
    nums = [-7,-3,2,3,11]
    obj = Solution()
    print(obj.sortedSquares(nums))