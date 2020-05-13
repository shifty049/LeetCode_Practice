class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        count=0
        for i in range(0,len(grid)-2):
            for j in range(0,len(grid[0])-2):
                
                check= [a[j:j+3] for a in grid[i:i+3]]
                
                if check[1][1]!=5:
                    pass
                
                
                elif all([sum(i)==15 for i in check]) & all([sum(i)==15 for i in list(zip(*check))]) and sorted([i for j in check for i in j])==list(range(1,10,1)):
                    count+=1
            
        return count

#Runtime: 32 ms, faster than 89.66% of Python3 online submissions for Magic Squares In Grid.
#Memory Usage: 14.1 MB, less than 33.33% of Python3 online submissions for Magic Squares In Grid.
#Fu-Ti, Hsu 
#shifty049@gmail.com

