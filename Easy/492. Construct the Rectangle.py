class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        s=int(area**(1/2)//1)
        while s>0:
            
            if not area%s:
                return(area//s,s)
            s-=1
#Runtime: 24 ms, faster than 97.53% of Python3 online submissions for Construct the Rectangle.
#Memory Usage: 13.9 MB, less than 16.67% of Python3 online submissions for Construct the Rectangle.
#Fu-Ti, Hsu 
#shifty049@gmail.com
