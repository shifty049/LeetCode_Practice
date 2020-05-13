class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:       
        if not ops:
            return m*n   
        min_i,min_j=min([i[0] for i in ops]),min([i[1] for i in ops])        
        return min_i*min_j
    
#Runtime: 68 ms, faster than 81.14% of Python3 online submissions for Range Addition II.
#Memory Usage: 15.7 MB, less than 33.33% of Python3 online submissions for Range Addition II.
#Fu-Ti, Hsu 
#shifty049@gmail.com