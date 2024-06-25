"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) < 3:
            return result

        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return result

        # if nums length > 3


        return result

    def threeSum_nlogn(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) < 3:
            return result

        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return result

        # if nums length > 3
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                res_list = []
                temp = nums[i] + nums[j]
                if -temp in nums[j+1:]:
                    res_list = [nums[i], nums[j], -temp]
                if res_list and sorted(res_list) not in result:
                    result.append(sorted(res_list))

        return result


if __name__ == '__main__':
    obj = Solution()
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [1, 2, -2, -1]
    # nums = [0, 0, 0, 0]
    print(obj.threeSum(nums))
