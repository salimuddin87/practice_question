"""
Given an array of strings words and a width maxWidth, format the text such that
each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line does not divide evenly between words, the empty
slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is
inserted between words.
"""
from typing import List


class Solution:
    def normalizeLine(self, arr: List[str], spaceNeeded: int, maxWidth: int, lastLine=False):
        resStr = ''
        l = len(arr)
        if l == 1:
            return arr[0] + ' ' * spaceNeeded

        if lastLine:
            for i in range(0, l):
                if i == l - 1:
                    if spaceNeeded <= 2:
                        resStr += ' ' * spaceNeeded
                        resStr += arr[i]
                    else:
                        resStr += arr[i] + ' ' * spaceNeeded
                else:
                    resStr += arr[i] + ' '
                    spaceNeeded -= 1

            return resStr

        # if length is more than one
        spacegiven = [0] * (l - 1)
        i = count = 0
        while count < spaceNeeded:
            if i == l - 2 and count + 1 <= spaceNeeded:
                spacegiven[i] += 1
                i = 0
                count += 1
            elif count + 1 <= spaceNeeded:
                spacegiven[i] += 1
                i += 1
                count += 1

        print(count, spacegiven, spaceNeeded)

        for i in range(0, l):
            if i != l - 1:
                resStr += arr[i] + ' ' * spacegiven[i]
                spaceNeeded -= spacegiven[i]
            else:
                resStr += arr[i].rstrip()

        print(resStr)
        return resStr

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tempArr = []
        resultArr = []
        l_tempArr = 0
        singleSpace = 0
        lenWords = len(words)

        for i in range(0, lenWords):

            if l_tempArr + len(words[i]) <= maxWidth:
                tempArr.append(words[i])
                l_tempArr += len(words[i]) + 1
                singleSpace += 1
            else:
                spaceNeeded = maxWidth - (l_tempArr - singleSpace)
                resultArr.append(self.normalizeLine(tempArr, spaceNeeded, maxWidth))
                tempArr.clear()
                tempArr.append(words[i])
                l_tempArr = len(words[i]) + 1
                singleSpace = 1

        if tempArr:
            spaceNeeded = maxWidth - (l_tempArr - singleSpace)
            resultArr.append(self.normalizeLine(tempArr, spaceNeeded, maxWidth, lastLine=True))

        return resultArr


if __name__ == '__main__':
    obj = Solution()

    # Example 1
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    # Expected Output:
    # [
    #    "This    is    an",
    #    "example  of text",
    #    "justification.  "
    # ]
    # print(obj.fullJustify(words, maxWidth))

    # Example 2
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    # Expected Output:
    # [
    #   "What   must   be",
    #   "acknowledgment  ",
    #   "shall be        "
    # ]
    print(obj.fullJustify(words, maxWidth))

    # Example 3
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    # Expected Output:
    # [
    #   "Science  is  what we",
    #   "understand      well",
    #   "enough to explain to",
    #   "a  computer.  Art is",
    #   "everything  else  we",
    #   "do                  "
    # ]
    # print(obj.fullJustify(words, maxWidth))

    # Example 4
    words = ["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do", "for",
     "your", "country"]
    maxWidth = 16
    # Output
    # ["ask   not   what","your country can","do  for  you ask","what  you can do","for your country"]...
    # print(obj.fullJustify(words, maxWidth))
