class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visited = {}
        
        def helper(loc):
            global bot_x
            global right_j
            if not visited.get(loc):
                if loc[0] > bot_x:
                    bot_x = loc[0]
                if loc[1] > right_j:
                    right_j = loc[1]
                
                visited[loc] = True
                new_land_group[loc] = True
                for x, y in [[0, 1], [1, 0]]:

                    new_x, new_y = loc[0] + x,  loc[1] + y

                    if  new_x < len(land) and new_y < len(land[0]):
                        
                        if land[new_x][new_y]:
                            helper((new_x, new_y))
        ans = []                                      
        for i in range(len(land)):
            
            for j in range(len(land[0])):
                
                if land[i][j]:
                    global bot_x
                    global right_j
                    upper_left = (i, j)
                    bot_x = i
                    right_j = j
                    new_land_group = {}
                    helper((i, j))
                    
                    if (bot_x, right_j) in new_land_group and (bot_x - i + 1) * (right_j - j + 1) == len(new_land_group):
                        ans.append([i, j, bot_x, right_j])               
        
        return ans

#Runtime: 1616 ms, faster than 48.09% of Python3 online submissions for Find All Groups of Farmland.
#Memory Usage: 38.7 MB, less than 31.55% of Python3 online submissions for Find All Groups of Farmland.
#Fu-Ti, Hsu 
#shifty049@gmail.com