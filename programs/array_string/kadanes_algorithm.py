"""
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number)
which has the maximum sum and return its sum. For example,
Input:
    N = 5
    Arr[] = {1,2,3,-2,5}
Output:
    9
    Explanation:
        Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.
-------------------------------------------------
Input:
    N = 4
    Arr[] = {-1,-2,-3,-4}
Output:
    -1
    Explanation:
        Max subarray sum is -1 of element (-1)
"""

from typing import List


def kadane_algorithm(arr: List[int]):
    max_ending_here = max_so_far = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = kadane_algorithm(arr)
    print("Maximum sum subarray:", max_sum)
