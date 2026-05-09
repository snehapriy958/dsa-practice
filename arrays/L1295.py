'''
Problem: Find Numbers with Even Number of Digits
Platform: LeetCode (1295)
Difficulty: Easy
Approach: String Conversion + Modulo Check
Time Complexity: O(n * d) where n is the number of elements and d is the number of digits in the largest number
Space Complexity: O(1) if we ignore the space used for string conversion

'''

class Solution:
    def findNumbers(self, nums: list) -> int:
        count = 0
        for num in nums:
            if len(str(num))%2 == 0:
                count += 1
        return count


if __name__ == '__main__':
    nums = [12,345,2,6,7896]
    obj = Solution()
    print(obj.findNumbers(nums))