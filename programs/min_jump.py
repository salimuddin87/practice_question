"""
Given an array arr[] of size n of non-negative integers. Each array element represents the maximum length of the jumps that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.


Examples :

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}, n = 11
Output: 3
Explanation:First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last.
Input: arr = {1, 4, 3, 2, 6, 7}, n = 6
Output: 2
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.

Your task:
You don't need to read input or print anything. Your task is to complete function minJumps() which takes the array arr and it's size n as input parameters and returns the minimum number of jumps. If not possible return -1.


Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
"""


class Solution:
    def minJumps(self, arr, n):
        # code here
        res = jump = 0
        count_jump = 0
        max_jump_index = 0
        i = 0
        while i < n:
            if arr[i] == 0:
                return -1
            for j in range(i+1, arr[i]):
                jump = j + arr[j]
                if res < jump:
                    res = jump
                    max_jump_index = j
            i = max_jump_index
            count_jump += 1
        return count_jump


if __name__ == '__main__':
    # T = int(input())
    # for i in range(T):
    #     n = int(input())
    #     Arr = [int(x) for x in input().split()]
    #     ob = Solution()
    #     ans = ob.minJumps(Arr, n)
    #     print(ans)

    # Expected jump is 4
    n = 76
    Arr = [10, 14, 29, 21, 17, 4, 18, 20, 18, 22, 21, 14, 27, 12, 3, 28, 17, 0, 2, 18, 8, 20, 26, 16, 9, 23, 25, 20,
           7, 27, 5, 7, 16, 5, 25, 11, 3, 7, 2, 17, 14, 6, 12, 14, 23, 25, 26, 5, 18, 1, 6, 10, 9, 12, 2, 25, 29, 12,
           19, 4, 8, 5, 8, 30, 2, 22, 24, 30, 7, 24, 8, 15, 16, 2, 11, 20]
    obj = Solution()
    ans = obj.minJumps(Arr, n)
    print(ans)
