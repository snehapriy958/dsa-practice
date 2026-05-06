class Solution:
    def removeDuplicates(self, nums: list) -> int:
        nums[:] = set(nums)
        nums.sort()
        return len(nums)
    
if __name__ == '__main__':
    nums = [-1,0,0,0,0,3,3]
    obj = Solution()
    print(obj.removeDuplicates(nums),", nums =",nums)