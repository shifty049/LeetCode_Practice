class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
             
        lst = sorted([a,b,c])
       
        mn,md,mx = lst
        
        score = 0
        
        diff = min(mx-md, mn)
        score += diff
        mx -= diff
        mn -= diff
        
        if not mn:
            return score + min(mx, md)
        
        d,r = divmod(mn,2)
        
        return score + mx - (d+r) + mn

#Runtime: 24 ms, faster than 98.77% of Python3 online submissions for Maximum Score From Removing Stones.
#Memory Usage: 14.3 MB, less than 55.46% of Python3 online submissions for Maximum Score From Removing Stones.
#Fu-Ti, Hsu 
#shifty049@gmail.com