class Solution:
    def maxArea(self, height: List[int]) -> int:
             
        left = 0
        
        right = len(height) - 1
        
        max_area = 0
        
        while left < right:
            
            area = min(height[left], height[right]) * (right - left)
            
            if area > max_area:
                
                max_area = area
            
            if height[left] < height[right]:
                
                left += 1
            
            elif height[left] > height[right]:
                
                right -= 1
            
            else:
                left += 1
                right -= 1
        
        return max_area

#Runtime: 712 ms, faster than 60.29% of Python3 online submissions for Container With Most Water.
#Memory Usage: 26 MB, less than 84.08% of Python3 online submissions for Container With Most Water.
#Fu-Ti, Hsu 
#shifty049@gmail.com
