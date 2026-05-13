'''
Problem: 1674. Minimum Moves to Make Array Complementary
Platform: LeetCode (1674)
Difficulty: medium
Approach: Difference Array + Prefix Sum
Time Complexity: O(n + m) where n is the length of nums and m is the
Space Complexity: O(m) for the difference array, where m is 2 * limit + 1

'''


from itertools import accumulate

class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        
        d = [0] * (2 * limit + 2)
        n = len(nums)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            low = min(a, b) + 1
            high = max(a, b) + limit
            target_sum = a + b
            d[2] += 2
            d[low] -= 1         
            d[target_sum] -= 1  
            d[target_sum + 1] += 1
            d[high + 1] += 1               
    
        return min(accumulate(d[2 : 2 * limit + 1]))
