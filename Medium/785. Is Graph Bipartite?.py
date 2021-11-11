class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        group_lst = [0 for _ in range(len(graph))]
        
        for ix, i in enumerate(graph):
            
            if group_lst[ix] == 0:
                
                group_lst[ix] = 1
                
                adj = -1
                
                queue =  i
                while queue:
                    # print(group_lst)
                    new_queue = []

                    for j in queue:

                        if group_lst[j] == 0:

                            group_lst[j] = adj 

                            for item in graph[j]:

                                if not group_lst[item]:
                                    new_queue.append(item)
                        else:

                            if group_lst[j] != adj:
                                return False
                    adj = 1 if adj == -1 else -1
                    queue = new_queue
                    
        return True

#Runtime: 168 ms, faster than 93.30% of Python3 online submissions for Is Graph Bipartite?.
#Memory Usage: 14.9 MB, less than 33.86% of Python3 online submissions for Is Graph Bipartite?.
#Fu-Ti, Hsu 
#shifty049@gmail.com