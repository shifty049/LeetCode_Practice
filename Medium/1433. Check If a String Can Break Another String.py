class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        ix=0
        a=sorted([ord(i) for i in s2])
        b=sorted([ord(i) for i in s1])
        dire=None
        while ix<len(s1):
            
            if not a[ix]-b[ix]:
                pass           
            else:
                if not dire:
                    dire=a[ix]-b[ix]
                
                if (a[ix]-b[ix])*dire<0:
                    return False            
            ix+=1        
        return True

#Runtime: 172 ms, faster than 73.80% of Python3 online submissions for Check If a String Can Break Another String.
#Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions for Check If a String Can Break Another String.
#Fu-Ti, Hsu 
#shifty049@gmail.com