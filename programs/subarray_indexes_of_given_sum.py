"""
Find Indexes of a subarray with given sum:
Write a function subarraySum() which takes arr, N, and S as input parameters and returns
an ArrayList containing the starting and ending positions of the first such occurring
subarray from the left where sum equals to S. The two indexes in the array should be
according to 1-based indexing. If no such subarray is found, return an array consisting
of only one element that is -1.
Input:
    N = 10, S = 15
    A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
    Explanation: The sum of elements from 1st position to 5th position is 15.
"""


# Time Complexity: O(n log n)
def subArraySum(arr, n, s):
    for row in range(0, n):
        for col in range(row+1, n+1):
            arr_sum = sum(arr[row:col])
            if arr_sum == s:
                return [row+1, col]
    return [-1]


# Time Complexity: O(n)
def sub_array_sum(arr, n, s):
    i = 0
    for j in range(1, n+1):
        arr_sum = sum(arr[i:j])
        while arr_sum > s and i < j:
            i += 1
            if i < j:
                arr_sum = sum(arr[i:j])
        if arr_sum == s:
            return [i+1, j]
    return [-1]


if __name__ == '__main__':
    n = 42
    s = 468
    arr = [135, 101,170,125,79,159,163,65,106,146,82,28,162,92,196,143,28,37,192,5,103,154,93,183,22,117,119,96,48,127,172,139,70,113,68,100,36,95,104,12,123,134]
    # print(subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15))
    # print(subArraySum([0], 1, 0))

    print(sub_array_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15))
    print(sub_array_sum([0], 1, 0))
    print(sub_array_sum(arr, n, s))
    print(sub_array_sum([1, 2, 3, 4], 4, 0))
