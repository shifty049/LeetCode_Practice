class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
                                
        if len(nums)==1:
            return nums
        nums.sort()        
        L=[]
        while sum(L)<=sum(nums):
            L.append(nums.pop())
            
        return L

#Runtime: 68 ms, faster than 52.66% of Python3 online submissions for Minimum Subsequence in Non-Increasing Order.
#Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Minimum Subsequence in Non-Increasing Order.
#Fu-Ti, Hsu 
#shifty049@gmail.com