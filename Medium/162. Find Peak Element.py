class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # at least two elements
        if len(nums)<2:
            return 0
        
        ix=1
        while ix<len(nums)-1:
            
            #return index of first peak if any
            if nums[ix]>nums[ix-1] and nums[ix]>nums[ix+1]:
                return ix
            ix+=1
        #return last index if the last element > the one before it
        if nums[-1]>nums[-2]:
            return len(nums)-1
        # not any peak found : return 0
        return 0

#Runtime: 40 ms, faster than 91.37% of Python3 online submissions for Find Peak Element.
#Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Find Peak Element.
#Fu-Ti, Hsu 
#shifty049@gmail.com