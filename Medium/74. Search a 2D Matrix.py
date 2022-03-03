class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        def binary_research(row, target):
            
            left, right = 0 ,len(row) - 1
            
            med = (left + right) // 2
            
            while right - left > 1:
                
                if row[med] > target:
                    
                    right = med
                
                elif row[med] < target:
                    
                    left = med
                
                else:
                    return True
                
                med = (left + right) // 2
            
            return row[left] == target or row[right] == target
        
        for row in matrix:
            
            if binary_research(row, target):
                return True
        return False

#Runtime: 47 ms, faster than 74.95% of Python3 online submissions for Search a 2D Matrix.
#Memory Usage: 14.4 MB, less than 96.11% of Python3 online submissions for Search a 2D Matrix.
#Fu-Ti, Hsu 
#shifty049@gmail.com