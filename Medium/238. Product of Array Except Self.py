class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        ans = [1] * n
        
        presix = 1
        postsix = 1
        
        for i in range(n):
            
            ans[i] *= presix
            ans[n - 1 - i] *= postsix
            
            presix  *= nums[i]
            
            postsix *= nums[n - 1 - i]
        
        return ans

#Runtime: 240 ms, faster than 69.19% of Python3 online submissions for Product of Array Except Self.
#Memory Usage: 21 MB, less than 80.78% of Python3 online submissions for Product of Array Except Self.
#Fu-Ti, Hsu 
#shifty049@gmail.com