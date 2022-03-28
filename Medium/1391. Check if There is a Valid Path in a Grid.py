class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        
        if m == n == 1:
            return True
        
        dic={1:{(0, 1), (0, -1)},
             2: {(1, 0), (-1, -0)},
             3: {(0, -1), (1, 0)}, 
             4: {(0, 1), (1, 0)},
             5: {(0, -1), (-1, 0)},
             6: {(-1, 0), (0, 1)}
            }
        
        
        q = [(0, 0)]
        visited = set()
        visited.add((0, 0))
        while q:
            new_q = []
            for nx, ny in q:
                for dx, dy in dic[grid[nx][ny]]:
                    new_nx, new_ny = nx + dx, ny + dy
                    
                    if  0 <= new_nx < m and 0 <= new_ny < n and (new_nx, new_ny) not in visited and (-dx, -dy) in dic[grid[new_nx][new_ny]]:
                        if new_nx == m - 1 and new_ny == n - 1:
                            return True
                        visited.add((new_nx, new_ny))
                        new_q.append((new_nx, new_ny))
            
            q = new_q
        
        return False

#Runtime: 1508 ms, faster than 91.59% of Python3 online submissions for Check if There is a Valid Path in a Grid.
#Memory Usage: 29.6 MB, less than 66.82% of Python3 online submissions for Check if There is a Valid Path in a Grid.
#Fu-Ti, Hsu 
#shifty049@gmail.com