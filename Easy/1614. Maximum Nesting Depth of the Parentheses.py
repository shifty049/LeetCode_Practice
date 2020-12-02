class Solution:
    def maxDepth(self, s: str) -> int:
        
        maxer = 0
        count = 0
        
        ix = 0
        while ix < len(s) :
            
            if s[ix] == '(':
                count+=1
                maxer = max(maxer,count)
                
            if s[ix] == ')':
                count-=1
        
            ix+=1
        
        return maxer

#Runtime: 28 ms, faster than 82.22% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
#Memory Usage: 14.2 MB, less than 36.37% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.
#Fu-Ti, Hsu 
#shifty049@gmail.com