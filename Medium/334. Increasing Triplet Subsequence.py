class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        small_1st = float('inf')
        small_2nd = float('inf')
        
        for n in nums:
            
            if n < small_1st:
                small_1st = n
            
            if small_1st < n < small_2nd:
                small_2nd = n
            
            if n > small_2nd:
                return True
        return False

#Runtime: 584 ms, faster than 89.98% of Python3 online submissions for Increasing Triplet Subsequence.
#Memory Usage: 24.7 MB, less than 67.55% of Python3 online submissions for Increasing Triplet Subsequence.
#Fu-Ti, Hsu 
#shifty049@gmail.com