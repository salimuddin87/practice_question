"""

"""
from typing import List
from copy import deepcopy


class Solution:
    def isAnagram(self, str1, str2):
        if len(str1) != len(str2):
            return False

        freq1 = {}
        freq2 = {}

        for char in str1:
            freq1[char] = freq1.get(char, 0) + 1

        for char in str2:
            freq2[char] = freq2.get(char, 0) + 1

        return freq1 == freq2

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        visited_index = []

        for i in range(0, len(strs)):
            temp = []
            if i not in visited_index:
                temp.append(strs[i])
                visited_index.append(i)
                for j in range(i+1, len(strs)):
                    if self.isAnagram(strs[i], strs[j]):
                        temp.append(strs[j])
                        visited_index.append(j)
            if temp:
                res.append(temp)
        return res


if __name__ == '__main__':
    obj = Solution()
    # print(obj.isAnagram("ddddddddddg", "dgggggggggg"))

    # Example 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    # print(obj.groupAnagrams(strs))

    # Example 2
    strs = ["ddddddddddg", "dgggggggggg"]
    print(obj.groupAnagrams(strs))
