class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(i, j, can):
            for x in range(len(board)):
                if board[x][j] == str(can):
                    return False
            for y in range(len(board[0])):
                if board[i][y] == str(can):
                    return False
            block_x, block_y = i // 3, j // 3
            for x in range(block_x*3, block_x*3+3):
                for y in range(block_y*3, block_y*3+3):
                    if board[x][y] == str(can):
                        return False
            return True

        def helper(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    # find the next state we are going to solve
                    if board[i][j] == '.':
                        # for all candidates
                        for can in range(1,10):
                            # if valid
                            if isValid(i, j, can):
                                # try this partital solution
                                board[i][j] = str(can)
                                # continue exploring
                                # we make a judgement here for finding an ending point
                                if helper(board):
                                    return True
                                # backtrack
                                board[i][j] = '.'
                        # if none of candidates work, this should be end in advance
                        return False
            return True
        helper(board)