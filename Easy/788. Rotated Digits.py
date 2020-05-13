class Solution:
    def rotatedDigits(self, N: int) -> int:
        count=0
        for i in range(1,N+1):
            if not {'3','4','7'}&set(str(i)) and {'2','5','6','9'}&set(str(i)):
            
                count+=1
            
        return count

#Runtime: 96 ms, faster than 54.84% of Python3 online submissions for Rotated Digits.
#Memory Usage: 13.7 MB, less than 50.00% of Python3 online submissions for Rotated Digits.
#Fu-Ti, Hsu 
#shifty049@gmail.com