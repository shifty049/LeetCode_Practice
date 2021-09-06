class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        q = list(range(1, n + 1))
        
        idx = 0
        while len(q) > 1:
            
            idx = (idx + k - 1) % len(q)
            
            q.pop(idx)
        
        return q[0]

#Runtime: 28 ms, faster than 94.55% of Python3 online submissions for Find the Winner of the Circular Game.
#Memory Usage: 14.2 MB, less than 74.80% of Python3 online submissions for Find the Winner of the Circular Game.
#Fu-Ti, Hsu 
#shifty049@gmail.com