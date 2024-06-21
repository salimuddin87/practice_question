"""


"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = len(nums)
        while k > l:
            k = k - l

        nums.reverse()
        # reverse first k element
        while i < (k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]
            i += 1

        j = k
        last = l - 1
        while j < (k + l)//2:
            nums[j], nums[last] = nums[last], nums[j]
            j += 1
            last -= 1


if __name__ == '__main__':
    obj = Solution()

    arr = [1, 2, 3, 4, 5, 6, 7]
    obj.rotate(arr, 3)
    print(arr)
