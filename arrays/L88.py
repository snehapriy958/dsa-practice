'''
Problem: Merge Sorted Array
Platform: LeetCode (88)
Difficulty: Easy
Approach: In-place Merge + Sorting
Time Complexity: O((m+n) log (m+n)) due to sorting (or O(m+n) if using a two-pointer approach)
Space Complexity: O(1) if we ignore the space used for sorting (or O(m+n) if using extra space for merging)

'''


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:]
        nums1.sort()

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    obj = Solution()
    obj.merge(nums1,m,nums2,n)
    print(nums1)