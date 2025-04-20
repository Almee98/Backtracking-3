# Time Complexity : O(m*n) * O(3^L) = O(m*n*3^L)
# Space Complexity : O(L)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# We will go through each cell of the board and check for the first letter of the word.
# If we find the first letter, we will perform a DFS from that cell to check if we can find the rest of the letters of the word.
# The DFS will check the following:
# 1. If we are out of bounds of the board.
# 2. If we have already visited the cell (we will mark it as visited by replacing it with a '#').
# 3. If the current cell does not match the letter we are looking for, it means we cannot find the word from this cell.
# 4. If we reach the end of the word, it means we have found the word and we will return True.
# 5. If we have not found the word, we will backtrack by replacing the visited cell with the original letter.

class Solution:
    def exist(self, board, word: str) -> bool:
        # Get the dimensions of the board
        m, n = len(board), len(board[0])
        # Define the directions for moving up, left, down, and right
        dirs = [[-1,0], [0,-1], [1,0], [0,1]]

        # DFS function to check if we can find the word starting from cell (i, j) at position p in the word
        def dfs(i, j, p):
            # base case
            # If the pointer p has reached the end of the word, it means we have found the word
            if p == len(word):
                # So we return True
                return True
            
            # If we are out of bounds of the board or if we have already visited the cell or if the current cell does not match the letter we are looking for, we return False
            if i<0 or j<0 or i==m or j==n or board[i][j] == "#":
                return False
            # If the current cell does not match the letter we are looking for, we return False
            if board[i][j] != word[p]:
                return False

            # action
            # If we reach here, it means that the current cell matches the letter we are looking for
            # So we will mark the cell as visited by replacing it with '#'
            board[i][j] = "#"

            # Now we will check the four directions (up, left, down, right) for the next letter in the word
            for row, col in dirs:
                r = i+row
                c = j+col
                # recurse
                # If we find the next letter in any of the four directions, we will return True
                if dfs(r, c, p+1):
                    return True

            # backtrack
            # If we reach here, it means we have not found the word in any of the four directions
            # So we will backtrack by replacing the visited cell with the original letter
            board[i][j] = word[p]
            # and return False
            return False

        # Iterate through each cell of the board and check for the first letter of the word
        for i in range(m):
            for j in range(n):
                # If we find the first letter, we will perform a DFS from that cell to check if we can find the rest of the letters of the word
                if board[i][j] == word[0]:
                    # If the DFS returns True, it means we have found the word, so we return True
                    if dfs(i, j, 0):
                        return True
        # If we have checked all the cells and have not found the word, we return False
        return False