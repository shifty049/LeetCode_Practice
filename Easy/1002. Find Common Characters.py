class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        l = []
        for i in set(A[0]):
            
            mn = min([item.count(i) for item in A])
                
            l+=mn*[i]
        
        return l

#Runtime: 36 ms, faster than 98.79% of Python3 online submissions for Find Common Characters.
#Memory Usage: 14.2 MB, less than 11.06% of Python3 online submissions for Find Common Characters.
#Fu-Ti, Hsu 
#shifty049@gmail.com