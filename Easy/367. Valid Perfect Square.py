class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        upper=num//2+1
        lower=1
        while upper-lower>1:
            middle=(upper+lower)//2
            
            if middle**2>num:
                upper=middle
            
            elif middle**2<num:
                lower=middle
            else:
                return True  
        return False
#Runtime: 28 ms, faster than 73.07% of Python3 online submissions for Valid Perfect Square.
#Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for Valid Perfect Square.
#Fu-Ti, Hsu 
#shifty049@gmail.com