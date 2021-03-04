class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        dic = {}
        
        for ix,i in enumerate(equations):
            if i[0] not in dic:
                dic[i[0]] = {}
                
            dic[i[0]].update( {i[1]: values[ix]})
            if  i[1] not in dic:
                dic[i[1]] = {}
            dic[i[1]].update( {i[0]: 1/values[ix]})
            
        ans = []
        for i in queries:
            if i[0] not in dic or i[1] not in dic:
                
                ans.append(-1.0)
            
            elif i[0] == i[1]:
                 ans.append(1.0)
            else:
                if i[1] in dic[i[0]]:             
                    ans.append(dic[i[0]][i[1]])
                else:
                    queue = [[key,value] for key,value in dic[i[0]].items()]

                    check = False
                    for ix in range(len(dic)):
                        new_queue = []

                        if queue:    
                            if check:
                                break
                            for node in queue:
                                if check:
                                    break
                                for key,value in dic[node[0]].items():
                                    if key != i[0]:

                                        if key == i[1]:
                                            ans.append(value*node[1])
                                            check = True
                                            break
                                        else:
                                            new_queue.append([key, value*node[1]])

                            queue = new_queue

                    if not check:
                        ans.append(-1.0)

        return ans

#Runtime: 20 ms, faster than 99.53% of Python3 online submissions for Evaluate Division.
#Memory Usage: 14.4 MB, less than 21.25% of Python3 online submissions for Evaluate Division.
#Fu-Ti, Hsu 
#shifty049@gmail.com