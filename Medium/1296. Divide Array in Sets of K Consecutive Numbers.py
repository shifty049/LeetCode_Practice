# Python3 solution using collections.Counter
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        if len(nums)%k!=0:
            return False
        ct=Counter(nums)
        for i in range(len(nums)//k):          
            s=min(ct.keys())
            if len(set(range(s,s+k))-set(ct.keys()))==0:
                ct=ct-Counter(range(s,s+k))
            else:
                return False
                                            
        return True   

#Runtime: 636 ms, faster than 12.77% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
#Memory Usage: 32.9 MB, less than 100.00% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
#Fu-Ti, Hsu 
#shifty049@gmail.com