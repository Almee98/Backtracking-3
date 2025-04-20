# Time Complexity : O(N!)
# Space Complexity : O(N^2)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# We will go through each column of each row and check if we can place a queen in that column.
# If we can place a queen, we will place it and recursively move to the next row.
# If we reach past the last row, it means we have placed all queens successfully and we will add the current board to the result.
# We will also check if we can place a queen in the current column by checking the following:
# 1. If there is a queen in the same column in the previous rows.
# 2. If there is a queen in the diagonal left up in the previous rows.
# 3. If there is a queen in the diagonal right up in the previous rows.
# We will use a 2D array to represent the chessboard and mark the cells where we have placed queens as True.

class Solution:
    def solveNQueens(self, n: int):
        # Initializing the result list and the chessboard
        res = []
        # Creating a chessboard of size n x n with all cells initialized to False
        chessboard = [[False for _ in range(n)] for _ in range(n)]

        # Function to check if we can place a queen at the given row and column
        def isValid(chessboard, row, col):
            # straight up
            i, j = row, col
            while i > 0:
                i -= 1
                if chessboard[i][j] == True:
                    return False
            # diagonal left up
            i, j = row, col
            while i>0 and j>0:
                i -= 1
                j -= 1
                if chessboard[i][j] == True:
                    return False
            # diagonal right up
            i, j = row, col
            while i>0 and j<n-1:
                i -= 1
                j += 1
                if chessboard[i][j] == True:
                    return False
            # If no queens are found in the same column or diagonals, we can place the queen in the current cell
            return True

        # Recursive function to perform DFS and place queens
        def dfs(row):
            # base case: if we have placed queens in all rows
            if row == n:
                # Create a board representation of the current solution
                board = []
                # Iterate through the chessboard and create a string representation of each row
                for i in range(n):
                    board_row = ""
                    for j in range(n):
                        if chessboard[i][j] == True:
                            board_row += "Q"
                        else:
                            board_row += "."
                    # Append the row string to the board
                    board.append(board_row)
                # Append the current board to the result list
                res.append(board)
                return

            # Iterate through each column in the current row
            for i in range(n):
                # Check if we can place a queen in the current column
                if isValid(chessboard, row, i):
                    # action
                    # Place the queen in the current cell
                    chessboard[row][i] = True
                    # recurse
                    # Move to the next row and try to place a queen
                    dfs(row+1)
                    # backtrack
                    # Remove the queen from the current cell
                    chessboard[row][i] = False
        # Start the DFS from the first row
        dfs(0)
        # Return the result list containing all valid solutions
        return res
    
# Approach: Place queens in each row while iterating through each column.
class Solution:
    def solveNQueens(self, n: int):
        res = []
        chessboard = [[False for _ in range(n)] for _ in range(n)]
        # Function to check if we can place a queen at the given row and column
        def isValid(chessboard, col, row):
            # straight left
            i, j = row, col
            while j > 0:
                j -= 1
                if chessboard[i][j] == True:
                    return False
            # diagonal left up
            i, j = row, col
            while i>0 and j>0:
                i -= 1
                j -= 1
                if chessboard[i][j] == True:
                    return False
            # diagonal left down
            i, j = row, col
            while i<n-1 and j>0:
                i += 1
                j -= 1
                if chessboard[i][j] == True:
                    return False
            # If no queens are found in the same row or diagonals, we can place the queen in the current cell
            return True
        # Recursive function to perform DFS and place queens
        def dfs(col):
            # base case: if we have placed queens in all columns
            if col == n:
                board = []
                for i in range(n):
                    board_row = ""
                    for j in range(n):
                        if chessboard[i][j] == True:
                            board_row += "Q"
                        else:
                            board_row += "."
                    board.append(board_row)
                res.append(board)
                return
            # Iterate through each row in the current column
            for i in range(n):
                # Check if we can place a queen in the current row
                if isValid(chessboard, col, i):
                    # action
                    # Place the queen in the current cell
                    chessboard[i][col] = True
                    # recurse
                    # Move to the next column and try to place a queen
                    dfs(col+1)
                    # backtrack
                    # Remove the queen from the current cell
                    chessboard[i][col] = False
        # Start the DFS from the first column
        dfs(0)
        # Return the result list containing all valid solutions
        return res