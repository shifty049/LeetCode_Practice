class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        max_len = 1        
        lens =1
        ix = 1
        
        if not nums:
            return 0
        
        while ix< len(nums):
            
            if nums[ix] > nums[ix-1]:
                lens+=1
                if lens > max_len:
                    max_len = lens
            else:
                lens =1
            
            ix+=1
            
        return max_len

#Runtime: 72 ms, faster than 95.21% of Python3 online submissions for Longest Continuous Increasing Subsequence.
#Memory Usage: 14.9 MB, less than 97.58% of Python3 online submissions for Longest Continuous Increasing Subsequence.
#Fu-Ti, Hsu 
#shifty049@gmail.com