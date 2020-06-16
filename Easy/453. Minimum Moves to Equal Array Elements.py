class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        return sum(nums)-len(nums)*min(nums)
    
#Runtime: 264 ms, faster than 75.09% of Python3 online submissions for Minimum Moves to Equal Array Elements.
#Memory Usage: 15 MB, less than 12.50% of Python3 online submissions for Minimum Moves to Equal Array Elements.
#Fu-Ti, Hsu 
#shifty049@gmail.com