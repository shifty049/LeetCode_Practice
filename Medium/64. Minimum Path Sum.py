class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

                elif i > 0:
                    grid[i][j] += grid[i - 1][j]

                elif j > 0:
                    grid[i][j] += grid[i][j - 1]
                                    
        return grid[-1][-1]

#Runtime: 100 ms, faster than 91.56% of Python3 online submissions for Minimum Path Sum.
#Memory Usage: 15.8 MB, less than 49.93% of Python3 online submissions for Minimum Path Sum.
#Fu-Ti, Hsu 
#shifty049@gmail.com