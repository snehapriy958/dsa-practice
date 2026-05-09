'''
Problem: Remove Duplicates from Sorted Array
Platform: LeetCode (26)
Difficulty: Easy    
Approach: Set Conversion + In-place Slice Assignment
Time Complexity: O(n log n) due to sorting (or O(n) if using a two-pointer approach)
Space Complexity: O(n) to store unique elements (or O(1) if using a

'''
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        nums[:] = set(nums)
        nums.sort()
        return len(nums)
    
if __name__ == '__main__':
    nums = [-1,0,0,0,0,3,3]
    obj = Solution()
    print(obj.removeDuplicates(nums),", nums =",nums)