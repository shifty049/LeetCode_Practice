class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        number = 0
        
        ix = 0
        while ix < len(arr):
            
            if arr[ix]%2:
                number += 1
                
                if number == 3:
                    return True
            
            else:
                number = 0
            ix += 1
        return False

#Runtime: 40 ms, faster than 96.50% of Python3 online submissions for Three Consecutive Odds.
#Memory Usage: 14 MB, less than 34.85% of Python3 online submissions for Three Consecutive Odds.
#Fu-Ti, Hsu 
#shifty049@gmail.com