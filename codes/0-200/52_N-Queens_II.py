class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        # typical backtrack problem
        # helper function to decide whether this is a valid move
        def isValid(idx, col, path):
            for i, p in enumerate(path):
                c = p.index('Q')
                if c == col:
                    return False
                if abs(i-idx) == abs(c-col):
                    return False
            return True

        def helper(idx, path):
            # if we reach the end/ we find a solution
            if idx == n:
                self.count += 1
                return
            # iterate over all candidates
            for col in range(n):
                if isValid(idx, col, path):
                    tmp = ['.'] * n
                    tmp[col] = 'Q'
                    # try this partial solution 
                    path.append(''.join(tmp))
                    # continue exploring
                    helper(idx+1, path)
                    # backtrack
                    path.pop()
        self.count = 0
        helper(0, [])
        return self.count