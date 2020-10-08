class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        q = [None]*len(s)
        
        for ix,i in enumerate(indices):
            q[i] = s[ix]
        
        return ''.join(q)

#Runtime: 48 ms, faster than 96.16% of Python3 online submissions for Shuffle String.
#Memory Usage: 14.1 MB, less than 5.04% of Python3 online submissions for Shuffle String.
#Fu-Ti, Hsu 
#shifty049@gmail.com