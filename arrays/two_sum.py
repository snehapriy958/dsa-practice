Class Solution:
    def twoSum(self, nums, target):
        mapp={}
        for i ,num in enumerate(nums):
            diff=target-num
            if diff in mapp:
                return[mapp[diff],i]
            mapp[num] =i