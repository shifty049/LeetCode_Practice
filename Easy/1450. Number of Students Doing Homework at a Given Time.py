class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        count=0
        
        for i in range(len(startTime)):
            if queryTime in range(startTime[i],endTime[i]+1):
                count+=1
        
        return count

#Runtime: 32 ms, faster than 94.08% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
#Memory Usage: 13.8 MB, less than 64.41% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
#Fu-Ti, Hsu 
#shifty049@gmail.com