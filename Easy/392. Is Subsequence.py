class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s=='':
            return True
        q=list(s)
        for ix,i in enumerate(t):            
            if i==q[0]:
                q.pop(0)
            if not q:
                return True
        
        return False

#Runtime: 144 ms, faster than 65.23% of Python3 online submissions for Is Subsequence.
#Memory Usage: 18.1 MB, less than 26.67% of Python3 online submissions for Is Subsequence.
#Fu-Ti, Hsu 
#shifty049@gmail.com