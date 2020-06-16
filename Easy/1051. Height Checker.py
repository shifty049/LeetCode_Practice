class Solution:
    def heightChecker(self, heights: List[int]) -> int:       
        return sum(list(map(lambda x,y:x!=y,heights,sorted(heights)))) 

#Runtime: 24 ms, faster than 98.37% of Python3 online submissions for Height Checker.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Height Checker.
#Fu-Ti, Hsu 
#shifty049@gmail.com