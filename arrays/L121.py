'''
Problem: Best Time to Buy and Sell Stock
Platform: LeetCode (121)
Difficulty: EasyApproach: One-pass / Greedy
Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf') # Track the lowest price seen so far
        max_profit = 0           # Track the highest profit found
        
        for price in prices:
            # Update min_price if the current price is a new low
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today yields a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
