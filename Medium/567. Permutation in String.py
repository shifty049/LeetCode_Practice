class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        lens1 = len(s1)
        lens2 = len(s2)
        c1 = [0]*26 
        c2 = [0]*26
        
        for i in s1:
            c1[ord(i) - ord('a')] += 1
        
        for i in s2[:lens1]:
            c2[ord(i) - ord('a')] += 1
            
        if c1 == c2:
            return True

        for i in range(lens1,lens2):
            
            c2[ord(s2[i]) - ord('a')] += 1
           
            c2[ord(s2[i - lens1]) - ord('a')] -= 1
            
            if c1 == c2:
                return True
          
        return False

#Runtime: 52 ms, faster than 98.40% of Python3 online submissions for Permutation in String.
#Memory Usage: 14.3 MB, less than 86.50% of Python3 online submissions for Permutation in String.
#Fu-Ti, Hsu 
#shifty049@gmail.com