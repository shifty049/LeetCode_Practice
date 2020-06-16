class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        return reduce(lambda x,y:x*y,[i-1 for i in sorted(nums)[-2:]])

#Runtime: 48 ms, faster than 91.15% of Python3 online submissions for Maximum Product of Two Elements in an Array.
#Memory Usage: 13.9 MB, less than 49.82% of Python3 online submissions for Maximum Product of Two Elements in an Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com