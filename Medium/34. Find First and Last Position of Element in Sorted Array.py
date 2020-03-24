class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos=[-1,-1]
        for ix,i in enumerate(nums):
            if i==target:

                #for first position : only recorded for once
                if pos[0]<0:
                    pos[0]=ix
                #for last position : continue to be updated    
                pos[1]=ix      
        return pos

#Runtime: 84 ms, faster than 89.04% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
#Memory Usage: 14 MB, less than 14.29% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com
