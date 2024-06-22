"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return l

        prev = nums[0]
        p_index = 0
        count = 1
        for i in range(1, l):
            curr = nums[i]
            if prev == curr:
                if count == 2:
                    continue
                else:
                    count = 2
                    p_index += 1
                    nums[p_index] = nums[i]
            else:
                p_index += 1
                nums[p_index] = nums[i]
                prev = nums[i]
                count = 1
        print(nums[:p_index+1])
        return p_index+1


if __name__ == '__main__':
    obj = Solution()
    # print(obj.removeDuplicates([1, 1, 1, 2, 2, 3]))
    # print(obj.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(obj.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 2, 2, 4]))
