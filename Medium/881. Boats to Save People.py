from collections import deque
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = deque(sorted(people))
        
        boat = 0
        
        while people:
            
            res = limit - people.pop()
            
            if people and res >= people[0]:
 
                people.popleft()
                    
            boat += 1
        
        return boat

#Runtime: 432 ms, faster than 96.88% of Python3 online submissions for Boats to Save People.
#Memory Usage: 21.5 MB, less than 7.54% of Python3 online submissions for Boats to Save People.
#Fu-Ti, Hsu 
#shifty049@gmail.com