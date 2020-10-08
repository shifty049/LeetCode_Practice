class Solution:
    def minOperations(self, n: int) -> int:
        
          
            if n%2: return (n-1)*(n+1)//4
           
            else: return  n*n//4

#Runtime: 28 ms, faster than 93.63% of Python3 online submissions for Minimum Operations to Make Array Equal.
#Memory Usage: 14 MB, less than 32.83% of Python3 online submissions for Minimum Operations to Make Array Equal.
#Fu-Ti, Hsu 
#shifty049@gmail.com
