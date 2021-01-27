class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
         
        area = 0
        dic = {tuple(p) : True for p in points}
        
        for idx, (x1, y1) in enumerate(points):
            
            for (x2, y2) in (points[idx+1:]):
                
                if (x2 - x1) * (y2 - y1) > 0:
                    
                    if (x1, y2) in dic and (x2, y1) in dic:
                        
                        if not area:
                            area = (x2 - x1) * (y2 - y1)
                        else:
                            area = min(area, (x2 - x1) * (y2 - y1))
                    
        return area

#Runtime: 1312 ms, faster than 55.34% of Python3 online submissions for Minimum Area Rectangle.
#Memory Usage: 14.7 MB, less than 60.53% of Python3 online submissions for Minimum Area Rectangle.
#Fu-Ti, Hsu 
#shifty049@gmail.com