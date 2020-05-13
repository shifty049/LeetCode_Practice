class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:        
            odd=0
            even=0
            for i in chips:
                if i%2:
                    odd+=1                    
                else: 
                    even+=1              
            return min(odd,even)

#Runtime: 32 ms, faster than 63.99% of Python3 online submissions for Play with Chips.
#Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Play with Chips.
#Fu-Ti, Hsu 
#shifty049@gmail.com