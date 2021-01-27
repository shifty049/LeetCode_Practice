class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        dic = {}
        for row in matrix:
            for choice in [tuple(row), tuple([int(i!=1) for i in row])]:
                
                if choice not in dic:
                    dic[choice] = 1
                else:
                    dic[choice] += 1
        
        return max(dic.values())

#Runtime: 1572 ms, faster than 71.74% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
#Memory Usage: 16.6 MB, less than 14.49% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
#Fu-Ti, Hsu 
#shifty049@gmail.com