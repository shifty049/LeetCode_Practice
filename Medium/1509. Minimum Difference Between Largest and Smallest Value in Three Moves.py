import math
from collections import Counter
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        
        if len(nums) <= 4:
            
            return 0
            
        miner = math.inf
        
        nums.sort()
        
        right = len(nums) - 1
        
        for left in range(0,4):
            
            miner = min(miner, nums[right - (3- left)] - nums[left])
            
        return miner

#Runtime: 332 ms, faster than 80.91% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
#Memory Usage: 24.1 MB, less than 41.95% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
#Fu-Ti, Hsu 
#shifty049@gmail.com
