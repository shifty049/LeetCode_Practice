class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]: 
        diff=sum(B)-sum(A)
        for i in set(A):        
            if (diff+2*i)/2 in set(B):
                return [i,(diff+2*i)/2]
#Runtime: 5660 ms, faster than 15.32% of Python3 online submissions for Fair Candy Swap.
#Memory Usage: 16.5 MB, less than 10.42% of Python3 online submissions for Fair Candy Swap.
#Fu-Ti, Hsu 
#shifty049@gmail.com