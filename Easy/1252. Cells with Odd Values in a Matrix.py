class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        origin=[[0]*m for _ in range(n)]
        

        for i in indices:
            origin[i[0]]=[i+1 for i in  origin[i[0]]]
            for jx in range(len(origin)):
                origin[jx][i[1]]+=1
                
        return sum([x%2 for x in [i for j in origin for i in j]])
                
#Runtime: 44 ms, faster than 64.86% of Python3 online submissions for Cells with Odd Values in a Matrix.
#Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Cells with Odd Values in a Matrix.
#Fu-Ti, Hsu 
#shifty049@gmail.com         
        