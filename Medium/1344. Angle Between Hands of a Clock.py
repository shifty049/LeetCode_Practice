class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hour_dgree=hour%12*30+minutes*0.5
        minutes_degree=minutes*6
        
        return min( abs(hour_dgree-minutes_degree),360-abs(hour_dgree-minutes_degree))

#Runtime: 24 ms, faster than 91.04% of Python3 online submissions for Angle Between Hands of a Clock.
#Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Angle Between Hands of a Clock.
#Fu-Ti, Hsu 
#shifty049@gmail.com