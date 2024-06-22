"""
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""
from typing import List
from copy import deepcopy


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = k = 0
        temp_nums1 = deepcopy(nums1)
        while k < m and j < n:

            if temp_nums1[k] <= nums2[j]:
                nums1[i] = temp_nums1[k]
                i += 1
                k += 1
            else:
                nums1[i] = nums2[j]
                j += 1
                i += 1

        while k < m:
            nums1[i] = temp_nums1[k]
            i += 1
            k += 1

        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1


if __name__ == '__main__':
    obj = Solution()
    nums = [4, 0, 0, 0, 0, 0]
    obj.merge(nums, 1, [1, 2, 3, 5, 6], 5)
    print(nums)
