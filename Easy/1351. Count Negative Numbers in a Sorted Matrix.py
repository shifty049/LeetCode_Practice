class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        #find out total number of elements < 0 in each row and sum them up
        return sum(list(map(lambda x: len(list(filter(lambda y:y<0,x))),grid)))

#Runtime: 124 ms, faster than 81.71% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
#Fu-Ti, Hsu 
#shifty049@gmail.com