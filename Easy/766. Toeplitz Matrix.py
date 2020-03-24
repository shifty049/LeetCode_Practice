class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(len(matrix)-1):
            
            for j in range(len(matrix[0])-1):
                
                if i+1<len(matrix) and j+1<len(matrix[0]):
                    if matrix[i+1][j+1]!=matrix[i][j]:
                        return False
        
        return True

#Runtime: 84 ms, faster than 88.82% of Python3 online submissions for Toeplitz Matrix.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Toeplitz Matrix.
#Fu-Ti, Hsu 
#shifty049@gmail.com