class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        l=[]
        for ix,idx in enumerate(index):
            l.insert(idx,nums[ix])
        return l

#Runtime: 32 ms, faster than 71.81% of Python3 online submissions for Create Target Array in the Given Order.
#Memory Usage: 14 MB, less than 12.31% of Python3 online submissions for Create Target Array in the Given Order.
#Fu-Ti, Hsu 
#shifty049@gmail.com