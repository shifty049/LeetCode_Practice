class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        
        current_length = 1
        current_check = s[0]
        maxer = cost[0]
        sum_cost = 0       
        ix = 1        
        s+=' '
        cost+=[0]
        while ix < len(s):
            if s[ix] == current_check:
                current_length += 1
                maxer = max(maxer, cost[ix])
            else:
                                
                if current_length > 1:
                    sum_cost += sum(cost[ix - current_length:ix]) - maxer  
                current_check = s[ix]
                current_length = 1
                maxer = cost[ix]
            ix+=1
               
        return sum_cost

#Runtime: 1076 ms, faster than 69.84% of Python3 online submissions for Minimum Deletion Cost to Avoid Repeating Letters.
#Memory Usage: 25.2 MB, less than 31.97% of Python3 online submissions for Minimum Deletion Cost to Avoid Repeating Letters.
#Fu-Ti, Hsu 
#shifty049@gmail.com