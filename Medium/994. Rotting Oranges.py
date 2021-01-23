class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        mins = 0
        
        dic = {0:[], 1:[],2:[]}
        
        for ix in range(len(grid)):
            for jx in range(len(grid[0])):             
                dic[grid[ix][jx]].append((ix, jx)) 
       
        
        if  dic[1] and not dic[2]:
            return -1
        all_rotten = not dic[1] 
           
        while not all_rotten:
            
            new = []
            for rotten in dic[2]:
               
                if rotten[0] -1 > -1 and grid[rotten[0] -1][rotten[1]] == 1 :
                    grid[rotten[0] -1][rotten[1]] =2
                    dic[1].remove((rotten[0] -1, rotten[1]))
                    new.append((rotten[0] -1, rotten[1]))
                
                if rotten[0] +1 < len(grid) and grid[rotten[0] +1][rotten[1]] == 1:
                    grid[rotten[0] +1][rotten[1]] = 2
                    dic[1].remove((rotten[0] +1, rotten[1]))
                    new.append((rotten[0] +1, rotten[1]))
                
                if rotten[1] +1 < len(grid[0]) and grid[rotten[0]][ rotten[1]+1] == 1:
                    grid[rotten[0]][rotten[1]+1] =2
                    dic[1].remove((rotten[0], rotten[1] +1))
                    new.append((rotten[0], rotten[1]+1))
                
                if rotten[1] -1 > -1 and grid[rotten[0]][rotten[1] -1] == 1:
                    
                    grid[rotten[0]][rotten[1] -1] =2
                    dic[1].remove((rotten[0], rotten[1] -1))
                    new.append((rotten[0], rotten[1]-1))
                
                else:
                    pass

            if not new and dic[1]:
                return -1
            
            dic[2] = new
               
            mins += 1
            
            all_rotten = not dic[1]
        return mins

#Runtime: 48 ms, faster than 87.58% of Python3 online submissions for Rotting Oranges.
#Memory Usage: 14.4 MB, less than 38.76% of Python3 online submissions for Rotting Oranges.
#Fu-Ti, Hsu 
#shifty049@gmail.com