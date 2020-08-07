class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        count=0
        max_d={i:max(grid[i]) for i in range(len(grid))}
        grid_z=list(zip(*grid))
        max_z_d={j:max(grid_z[j]) for j in range(len(grid_z))}
        for i in range(len(grid)):
            maxer=max_d[i]
            for j in range(len(grid[0])):
                maxer_z=max_z_d[j]
                if grid[i][j] not in [maxer,maxer_z]:
                    count+=min(maxer,maxer_z)-grid[i][j] if min(maxer,maxer_z)-grid[i][j]>0 else 0
    
        return count

#Runtime: 68 ms, faster than 94.67% of Python3 online submissions for Max Increase to Keep City Skyline.
#Memory Usage: 13.9 MB, less than 63.12% of Python3 online submissions for Max Increase to Keep City Skyline.
#Fu-Ti, Hsu 
#shifty049@gmail.com