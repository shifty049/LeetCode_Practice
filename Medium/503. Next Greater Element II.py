class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        nums*=2
        stack = []
        
        ans = [-1]* len(nums)
        
        for ix,i in enumerate(nums):
            
            while stack and nums[stack[-1]] < i:
                ans[stack.pop()] = i
            
            stack.append(ix)
        
        return ans[:len(nums)//2]

#Runtime: 208 ms, faster than 84.60% of Python3 online submissions for Next Greater Element II.
#Memory Usage: 15.9 MB, less than 30.08% of Python3 online submissions for Next Greater Element II.
#Fu-Ti, Hsu 
#shifty049@gmail.com
