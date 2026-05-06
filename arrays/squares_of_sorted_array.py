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