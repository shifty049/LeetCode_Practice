class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:        
        l=[]
        ix=0
        sumer=0
        while ix<len(nums):
            sumer+=nums[ix]
            l.append(sumer)
            ix+=1
        return l

#Runtime: 44 ms, faster than 87.24% of Python3 online submissions for Running Sum of 1d Array.
#Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Running Sum of 1d Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com