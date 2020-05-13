class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
            m=len(grid)
            n=len(grid[0])
            k%=m*n
            if not k:
                return grid
            
            result=[i for j in grid for i in j][-k:]+[i for j in grid for i in j][:-k]
            
            return [result[i*n:(i+1)*n] for i in range(m)]

#Runtime: 160 ms, faster than 94.54% of Python3 online submissions for Shift 2D Grid.
#Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Shift 2D Grid.
#Fu-Ti, Hsu 
#shifty049@gmail.com