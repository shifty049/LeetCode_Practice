class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        if m == n == 1:
            return 1
        
        q = [(0, 0)]
        
        visited = set()
        
        visited.add((0, 0))
        lev = 1
        while q:
            lev += 1
            new_q = []
            
            for lx, ly in q:
                for d_x, d_y in  [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i,j) != (0, 0)]:
                    new_x, new_y = lx + d_x,  ly + d_y
                    if 0 <= new_x < m and 0 <= new_y < n and not grid[new_x][new_y] and (new_x,  new_y) not in visited:
                        if (new_x,  new_y) == (m - 1, n - 1):
                            return lev
                        visited.add((new_x,  new_y))
                        new_q.append((new_x,  new_y))
                        
            q = new_q
                
        return -1

#Runtime: 985 ms, faster than 40.39% of Python3 online submissions for Shortest Path in Binary Matrix.
#Memory Usage: 15.4 MB, less than 43.65% of Python3 online submissions for Shortest Path in Binary Matrix.
#Fu-Ti, Hsu 
#shifty049@gmail.com