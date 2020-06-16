class Solution:
    def maxPower(self, s: str) -> int:        
        maxer=1
        starter=s[0]
        ix=1      
        length=1
        while ix<len(s):          
            if s[ix]==starter:
                length+=1
            else:
                starter=s[ix]
                maxer=max(maxer,length)
                length=1
            ix+=1
        maxer=max(maxer,length)     
        return maxer
#Runtime: 40 ms, faster than 89.26% of Python3 online submissions for Consecutive Characters.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Consecutive Characters.
#Fu-Ti, Hsu 
#shifty049@gmail.com