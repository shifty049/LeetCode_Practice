class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        maxer = 0
        lst = [0]
        
        for i in nums:
            if i == 1:
                lst[-1] +=1
            else:
                maxer = max(maxer,sum(lst[-2:]))
                lst.append(0)
      
        if len(lst) == 1:
            
            return lst[-1] - 1
        
        return max(sum(lst[-2:]),maxer)
                    
#Runtime: 352 ms, faster than 91.43% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
#Memory Usage: 16.7 MB, less than 50.13% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
#Fu-Ti, Hsu 
#shifty049@gmail.com
