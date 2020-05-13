class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        min_v=None
        sumer=0
        for i in nums:
            sumer+=i
            if not min_v:
                min_v=sumer
            else:
                min_v=min(min_v,sumer)
        
        return max(1-min_v,1)
#Runtime: 24 ms, faster than 96.28% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
#Fu-Ti, Hsu 
#shifty049@gmail.com