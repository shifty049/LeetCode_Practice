class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        a=sum([distance[i] for i in range(min(start,destination),max(start,destination))])
        
        return min(a,sum(distance)-a)

#Runtime: 44 ms, faster than 71.00% of Python3 online submissions for Distance Between Bus Stops.
#Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Distance Between Bus Stops.
#Fu-Ti, Hsu 
#shifty049@gmail.com