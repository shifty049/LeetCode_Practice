class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:        
        l=[]
        matrix_t=list(zip(*matrix))       
        for i in range(len( matrix)):            
            j=matrix[i].index(min(matrix[i]))              
            if matrix[i][j]==max(matrix_t[j]):
                l.append(matrix[i][j])                
        return l

#Runtime: 120 ms, faster than 99.64% of Python3 online submissions for Lucky Numbers in a Matrix.
#Memory Usage: 14.2 MB, less than 18.65% of Python3 online submissions for Lucky Numbers in a Matrix.
#Fu-Ti, Hsu 
#shifty049@gmail.com