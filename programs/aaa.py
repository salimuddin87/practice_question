from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            j, total_len = i, 0
            while j < len(words) and total_len + len(words[j]) + j - i <= maxWidth:
                total_len += len(words[j])
                j += 1
            if j == len(words):
                res.append(" ".join(words[i:j]) + " " * (maxWidth - total_len - (j - i - 1)))
            else:
                spaces = maxWidth - total_len
                slots = j - i - 1
                if slots == 0:
                    res.append(words[i] + " " * spaces)
                else:
                    spaces_per_slot = spaces // slots
                    extra_spaces = spaces % slots
                    line = words[i]
                    for k in range(i + 1, j):
                        line += " " * (spaces_per_slot + (1 if extra_spaces > 0 else 0))
                        extra_spaces -= 1
                        line += words[k]
                    res.append(line)
            i = j
        return res


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # list to store the justified lines
        justified_lines = []
        # list to store the current line of words
        line = []
        # length of the current line
        line_length = 0
        # loop through all words
        for word in words:
            # if adding the current word to the line and a space would exceed the maxWidth
            if line_length + len(word) + len(line) > maxWidth:
                # calculate the number of spaces needed to be added to the line
                spaces = maxWidth - line_length
                # distribute the spaces as evenly as possible between the words
                for i in range(spaces):
                    line[i % (len(line) - 1 or 1)] += ' '
                # add the line to the justified_lines list
                justified_lines.append(''.join(line))
                # reset line and line_length for the next line
                line = []
                line_length = 0
            # add the current word to the line
            line.append(word)
            line_length += len(word)
        # handle the last line, which is left-justified
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        justified_lines.append(last_line)
        return justified_lines
