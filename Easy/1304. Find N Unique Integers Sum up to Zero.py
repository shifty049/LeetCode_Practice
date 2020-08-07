class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        return list(range((1-n)//2,(n-1)//2+1)) if n%2 else list(range((-1*n//2),0))+ list(range(1,n//2+1))

#Runtime: 32 ms, faster than 70.93% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
#Memory Usage: 13.7 MB, less than 93.41% of Python3 online submissions for Find N Unique Integers Sum up to Zero.
#Fu-Ti, Hsu 
#shifty049@gmail.com