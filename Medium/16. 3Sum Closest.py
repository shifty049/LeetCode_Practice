import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        sumer = math.inf
        
        for i in range(len(nums) - 2):
            
            left = i+1
            
            right = len(nums) - 1
            
            
            while left < right:
                
                new_sumer = nums[i] + nums[left] + nums[right]
                
                diff = target - new_sumer
                
                if abs(diff) < abs(target - sumer):
                    
                    sumer = new_sumer
                
                if diff > 0:
                    
                    left += 1
                
                elif diff < 0:
                    
                    right -= 1
                
                else:
                    return target
            
        return sumer

#Runtime: 120 ms, faster than 76.19% of Python3 online submissions for 3Sum Closest.
#Memory Usage: 14.2 MB, less than 89.43% of Python3 online submissions for 3Sum Closest.
#Fu-Ti, Hsu 
#shifty049@gmail.com
