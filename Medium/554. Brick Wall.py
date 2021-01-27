class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        dic = {}
        
        for i in wall:
            cross = 0
            
            for j in i[:-1]:            
                cross += j            
                if cross not in dic:
                    dic[cross] = 1             
                else:
                    dic[cross] += 1       
        if not dic:
            return len(wall)
        
        return len(wall) - max(dic.values())

#Runtime: 168 ms, faster than 97.05% of Python3 online submissions for Brick Wall.
#Memory Usage: 19.2 MB, less than 24.68% of Python3 online submissions for Brick Wall.
#Fu-Ti, Hsu 
#shifty049@gmail.com