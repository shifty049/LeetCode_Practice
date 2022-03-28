class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.ans = [[None] * n for _ in range(m)]
        for ix in range(m):
            for jx in range(n):
                
                if not ix and not jx:
                     self.ans[ix][jx] = matrix[ix][jx]
                                    
                elif not ix:
                    
                    if jx:
                        self.ans[ix][jx] = matrix[ix][jx] + self.ans[ix][jx - 1]
                
                elif not jx:
                        if ix:
                            self.ans[ix][jx] = matrix[ix][jx] + self.ans[ix - 1][jx]
                
                else:
                    self.ans[ix][jx] = matrix[ix][jx] + self.ans[ix - 1][jx] + self.ans[ix][jx - 1] -  self.ans[ix - 1][jx - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        if row1 == col1 == 0:
            return self.ans[row2][col2]
        else:
            rtn = self.ans[row2][col2]
            
            if row1 and not col1:
                rtn -= self.ans[row1 - 1][col2]
            
            elif col1 and not row1:
                rtn -= self.ans[row2][col1 - 1]
            else:
                rtn -= (self.ans[row1 - 1][col2] + self.ans[row2][col1 - 1] - self.ans[row1 - 1][col1 - 1])
            
            return rtn
                
                
            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

#Runtime: 1520 ms, faster than 92.97% of Python3 online submissions for Range Sum Query 2D - Immutable.
#Memory Usage: 25 MB, less than 39.79% of Python3 online submissions for Range Sum Query 2D - Immutable.
#Fu-Ti, Hsu 
#shifty049@gmail.com
