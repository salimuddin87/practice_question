"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from typing import List


class Solution:
    valid_value = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    def validate_set(self, nums: List[str]):
        temp_list = []
        for i in range(0, len(nums)):
            if nums[i] == '.':
                continue
            elif nums[i] not in self.valid_value:
                return False
            elif nums[i] in temp_list:
                return False
            else:
                temp_list.append(nums[i])
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate all 9 rows
        for row in range(0, 9):
            # print(board[row])
            if not self.validate_set(board[row]):
                return False

        # validate all 9 columns
        for col in range(0, 9):
            board_col = [board[row][col] for row in range(0, 9)]
            print(board_col)
            if not self.validate_set(board_col):
                return False

        # validate 3X3 square
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                board_square = [board[x][y] for x in range(row, row+3) for y in range(col, col+3)]
                # print(board_square)
                if not self.validate_set(board_square):
                    return False

        # there must be at least 17 clues in order for
        # a Sudoku Board to have a unique solution.
        count = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] in self.valid_value:
                    count += 1
        if count < 17:
            return False

        return True


if __name__ == '__main__':
    obj = Solution()

    # Example 1:
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", "8", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    # Output: true
    # print(obj.isValidSudoku(board))

    # Example 2:
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # Output: false
    # print(obj.isValidSudoku(board))

    # Example 3:
    board = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]
    ]
    # Output: false
    print(obj.isValidSudoku(board))
