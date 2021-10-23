class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums.sort()
        
        ix = 1
        mx = 1
        so_far = 1
        nxt = nums[0] + 1
        while ix < len(nums):
            
            if nums[ix] == nxt:
                
                so_far += 1
                nxt += 1
            
            elif nums[ix] == nxt - 1:
                pass
            
            else:
                mx = max(mx, so_far)
                so_far = 1
                nxt = nums[ix] + 1
            ix += 1
        
        return max(mx, so_far)

#Runtime: 288 ms, faster than 48.54% of Python3 online submissions for Longest Consecutive Sequence.
#Memory Usage: 22.7 MB, less than 98.46% of Python3 online submissions for Longest Consecutive Sequence.
#Fu-Ti, Hsu 
#shifty049@gmail.com