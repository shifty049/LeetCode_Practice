class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        cost=sorted([[i[0]-i[1],ix] for ix,i in enumerate(costs)])
        
        return sum([costs[j[1]][0] for j in cost[:len(cost)//2]])+sum([costs[j[1]][1] for j in cost[-len(cost)//2:]])
            
#Runtime: 32 ms, faster than 95.00% of Python3 online submissions for Two City Scheduling.
#Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions for Two City Scheduling.
#Fu-Ti, Hsu 
#shifty049@gmail.com