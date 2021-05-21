class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        count = 0
        pd = 1
        left = 0
        
        for right in range(len(nums)):
            
            pd *= nums[right]
            
            if pd < k:
                count +=  right - left + 1
            
            else:
                
                while pd >= k and left < right:
                    
                    pd /= nums[left]
                    
                    left += 1
                    
                    if pd < k:
                        
                        break
     
                if pd < k:

                    count +=  right - left + 1
            
        return count

#Runtime: 1080 ms, faster than 73.61% of Python3 online submissions for Subarray Product Less Than K.
#Memory Usage: 18.6 MB, less than 70.93% of Python3 online submissions for Subarray Product Less Than K.
#Fu-Ti, Hsu 
#shifty049@gmail.com