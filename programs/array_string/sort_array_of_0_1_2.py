
class Solution:

    def sort0(self, arr, n, num1, num2):
        if num1 > num2:
            num1, num2 = num2, num1

        # Sort 0 and 1 in the array
        i = 0
        j = n - 1
        while i < j:
            while arr[i] != num2:
                i += 1
            while arr[j] != num1:
                j -= 1
            # Swap
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        # print(arr)

    def sort012(self, arr, n):
        # sort 0 and 1 in the array
        self.sort0(arr, n, 0, 1)
        # Sort 0 and 2 in the array
        self.sort0(arr, n, 0, 2)
        # sort 1 and 2 in the array
        self.sort0(arr, n, 1, 2)


if __name__ == '__main__':
    # n = 5  # int(input("Enter N value "))
    # arr = [2, 2, 1, 1, 0]  # [int(x) for x in input("Enter an array ").strip().split()]
    arr = [2, 0, 2, 0, 0, 1, 2, 2, 2, 1, 1, 0, 1, 1, 1, 2, 0, 1, 2, 1, 0, 1, 2, 0, 0, 0, 2, 0, 1, 0, 0, 0, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 1, 2, 0, 2, 0, 0, 1, 2, 1, 2, 1, 1, 2, 1, 2, 0, 0, 1, 0, 2, 1, 1, 2, 0, 2, 0, 1, 2, 2, 2, 2, 1, 0, 1, 2, 2, 0, 1, 1, 1, 0, 1, 2, 0, 0, 2, 1, 0, 0, 2, 2, 1, 0]
    ob = Solution()
    ob.sort012(arr, len(arr))
    print(arr)
    # for i in arr:
    #     print(i, end=' ')
    # print()
