class Solution:
    def reachNumber(self, target: int) -> int:
            
        def check(target, n):
            
            if n * (n + 1) / 2 > target:
                return True
            
            elif n * (n + 1) / 2 < target:
                return False
            else:
                return None
                
        
        target = abs(target)
        left = 0
        right = target + 1
        
        med = (left + right) // 2
        
        while right - left > 1:
            
            if check(target, med) is True:
                
                right = med
            elif check(target, med) is False:
               
                left = med
            else:
                return med
            
            med = (left + right) // 2
            
        if check(target, left):
            
            initial = left
        else:  
            initial = right
     
        diff = abs(abs(target - initial * (initial + 1) / 2))
        
        # diff is even
        if not diff % 2:
            step = initial
        else:
            if (initial + 1) % 2:
                step = initial + 1
            else:
                step = initial + 2
        
        return step

#Runtime: 31 ms, faster than 97.19% of Python3 online submissions for Reach a Number.
#Memory Usage: 13.9 MB, less than 64.04% of Python3 online submissions for Reach a Number.
#Fu-Ti, Hsu 
#shifty049@gmail.com