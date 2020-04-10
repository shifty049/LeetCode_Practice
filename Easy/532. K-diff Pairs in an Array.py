class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        
        if k<0:
            return 0
        if k==0:
            return len([i  for i in set(nums) if len(list(filter(lambda x:x==i,nums)))>1])

        
        nums=sorted(set(nums))
        
        return len([[i,i+k] for ix,i in enumerate(nums[:-1]) if i+k in nums[ix+1:]])

#Runtime: 1136 ms, faster than 10.05% of Python3 online submissions for K-diff Pairs in an Array.
#Memory Usage: 15.9 MB, less than 16.13% of Python3 online submissions for K-diff Pairs in an Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com
        