class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost)==1:
            return cost[0]
            
        dp=[None]*(len(cost)+1)
        for ix,i in enumerate( dp):
            
            if ix <2:
                dp[ix]=0
            
            else:
                dp[ix]=min(dp[ix-2]+cost[ix-2],dp[ix-1]+cost[ix-1])
          
        return dp[-1]
#Runtime: 52 ms, faster than 92.63% of Python3 online submissions for Min Cost Climbing Stairs.
#Memory Usage: 13.6 MB, less than 7.69% of Python3 online submissions for Min Cost Climbing Stairs.
#Fu-Ti, Hsu 
#shifty049@gmail.com