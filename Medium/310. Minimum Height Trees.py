class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:  
        
        if n == 1:
            return [0]
        
        dic = {i: [] for i in range(n)}
        
        for x, y in edges:
            
            dic[x].append(y)
            dic[y].append(x)
        
        queue = [x for x,y in dic.items() if len(y) == 1]
        
        while n > 2:
            
            n -= len(queue)
            
            new_queue = []
            for u in queue:
                
                v = dic[u][0]
                
                dic[v].remove(u)
                
                if len(dic[v]) == 1:
                    
                    new_queue.append(v)
            
            queue = new_queue 
        
        return queue

#Runtime: 228 ms, faster than 93.77% of Python3 online submissions for Minimum Height Trees.
#Memory Usage: 18.2 MB, less than 92.93% of Python3 online submissions for Minimum Height Trees.
#Fu-Ti, Hsu 
#shifty049@gmail.com
