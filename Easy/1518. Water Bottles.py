class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
                
        drink=0
        empty=0
        while numBottles:            
            drink+=1
            numBottles-=1
            empty+=1
            numBottles+=1 if not empty%numExchange else 0                          
        return drink

#Runtime: 24 ms, faster than 97.10% of Python3 online submissions for Water Bottles.
#Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Water Bottles.
#Fu-Ti, Hsu 
#shifty049@gmail.com