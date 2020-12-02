class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        
        max_wealth = 0
        
        for  people in accounts:
            max_wealth = sum(people)  if sum(people) > max_wealth else max_wealth
        
        return max_wealth

#Runtime: 52 ms, faster than 86.56% of Python3 online submissions for Richest Customer Wealth.
#Memory Usage: 14.2 MB, less than 65.41% of Python3 online submissions for Richest Customer Wealth.
#Fu-Ti, Hsu 
#shifty049@gmail.com