"""
Minimum Size Subarray Sum
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""


from typing import List
# from sys import maxsize


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = 0
        sum = 0
        l = 0
        while end < len(nums):
            sum += nums[end]
            while sum >= target:
                if l == 0:
                    l = end - start + 1
                else:
                    l = min(l, end - start + 1)
                sum -= nums[start]
                start += 1
            end += 1
        return l


if __name__ == '__main__':
    obj = Solution()
    print(obj.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(obj.minSubArrayLen(12, [1, 2, 3, 4, 5]))
    print(obj.minSubArrayLen(5, [1, 1, 1, 1]))
