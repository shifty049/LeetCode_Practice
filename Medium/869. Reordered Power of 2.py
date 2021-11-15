class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        start = 0
        while len(str(2 **(start))) <= len(str(n)):
            
            if len(str(2 **(start))) == len(str(n)):
                
                if sorted(str(2 **(start))) == sorted(str(n)):
                    return True
            
            start += 1
        
        return False

#Runtime: 24 ms, faster than 100.00% of Python3 online submissions for Reordered Power of 2.
#Memory Usage: 14.1 MB, less than 80.63% of Python3 online submissions for Reordered Power of 2.
#Fu-Ti, Hsu 
#shifty049@gmail.com