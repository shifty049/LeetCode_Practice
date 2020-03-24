class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        if len(set(B)-set(A))>0:
            return -1
        s=str(A)
        count=0        
        while len(s)<=len(A)*len(B):
            count+=1
            if B in s:
                return count
            s+=A
        return -1

#Runtime: 244 ms, faster than 10.01% of Python3 online submissions for Repeated String Match.
#Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Repeated String Match.
#Fu-Ti, Hsu 
#shifty049@gmail.com