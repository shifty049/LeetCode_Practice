class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        dic = {'row': set(), 'col': set()}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if not matrix[i][j]:
                    dic['row'].add(i)
                    dic['col'].add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if i in dic['row'] or j in dic['col']:
                    matrix[i][j] = 0
        
        return matrix

#Runtime: 140 ms, faster than 77.50% of Python3 online submissions for Set Matrix Zeroes.
#Memory Usage: 14.7 MB, less than 95.83% of Python3 online submissions for Set Matrix Zeroes.
#Fu-Ti, Hsu 
#shifty049@gmail.com
