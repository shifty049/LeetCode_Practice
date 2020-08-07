class Solution:
    def isPathCrossing(self, path: str) -> bool:        
        loc=[[0,0]]       
        for i in path:            
            if i in ['E','W']:
                loc_n=[loc[-1][0]+1 if i=='E' else loc[-1][0]-1,loc[-1][1]]
            else:
                loc_n=[loc[-1][0],loc[-1][1]+1 if i=='N' else loc[-1][1]-1]
            if loc_n in loc:
                return True
            loc.append(loc_n)
        return False
#Runtime: 24 ms, faster than 94.93% of Python3 online submissions for Path Crossing.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Path Crossing.
#Fu-Ti, Hsu 
#shifty049@gmail.com