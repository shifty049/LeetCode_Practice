class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ix = 2
        
        while ix < len(nums):
            
            if nums[ix] == nums[ix - 2]:
                
                nums.pop(ix - 2)
            
            else:
                ix += 1
        
        return len(nums)

#Runtime: 56 ms, faster than 49.18% of Python3 online submissions for Remove Duplicates from Sorted Array II.
#Memory Usage: 14.1 MB, less than 94.84% of Python3 online submissions for Remove Duplicates from Sorted Array II.
#Fu-Ti, Hsu 
#shifty049@gmail.com