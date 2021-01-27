class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        wait_time = 0
        time_start = 0
        for ix, [x,y] in enumerate(customers):
              
            time_start = max(time_start,x)
            
            wait_time += y + time_start - x
        
            time_start += y
        
        return wait_time / (ix+1)

#Runtime: 952 ms, faster than 61.60% of Python3 online submissions for Average Waiting Time.
#Memory Usage: 55.2 MB, less than 19.15% of Python3 online submissions for Average Waiting Time.
#Fu-Ti, Hsu 
#shifty049@gmail.com