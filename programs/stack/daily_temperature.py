"""
Given an array of integers temperatures represents the daily temperatures, return an array answer
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
from typing import List


class Solution:
    def daily_temperature(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        if len(temperatures) == 1:
            return result

        stack = []
        for i in range(0, len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                while stack:
                    index = stack.pop()
                    if temperatures[index] < temperatures[i]:
                        result[index] = i - index
                    else:
                        stack.append(index)
                        break
                stack.append(i)

        return result


if __name__ == '__main__':
    temperature = [73, 74, 75, 71, 69, 72, 76, 73]
    obj = Solution()
    print(obj.daily_temperature(temperature))
