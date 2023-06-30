# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# 一个经典的回溯题。从左到右，从上到下，依次填入数字，如果数字没有达到要求，则回溯到上一个位置，更改数字。

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(0, 9):
          for j in range(0, 9):

    def isValid(self, row, col, board, 
        
