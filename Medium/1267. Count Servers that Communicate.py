class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
             
        dic = {'col':{},'row':{}}
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    if i not in dic['row']:
                        dic['row'][i]= [str((i,j))]
                    else:   
                        dic['row'][i].append(str((i,j)))

                    if j not in dic['col']:
                        dic['col'][j] = [str((i,j))]
                    else:    

                        dic['col'][j].append(str((i,j)))
         
        ans = []

        for i in dic:
            
            for lst in dic[i].values():
                
                if len(lst) > 1:
                    
                    ans += lst
                    
        return len(set(ans))

#Runtime: 464 ms, faster than 90.41% of Python3 online submissions for Count Servers that Communicate.
#Memory Usage: 16.4 MB, less than 15.37% of Python3 online submissions for Count Servers that Communicate.
#Fu-Ti, Hsu 
#shifty049@gmail.com
