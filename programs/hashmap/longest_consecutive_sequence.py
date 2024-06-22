"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) solution
        res = 0
        num_set = set(nums)  # Convert the list to a set to allow O(1) time complexity for lookups.
        if not nums:
            return res

        for i in range(0, len(nums)):
            if nums[i] - 1 not in num_set:
                lc = 1
                temp = nums[i]
                while temp + 1 in num_set:
                    lc += 1
                    temp += 1
                res = max(res, lc)

        return res


if __name__ == '__main__':
    obj = Solution()
    print(obj.longestConsecutive([100,4,200,1,3,2]))
