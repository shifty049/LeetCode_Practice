class Solution:
    def checkRecord(self, s: str) -> bool:
        
        return s.count('A')<2 and 'L'*3 not in s
#Runtime: 28 ms, faster than 70.23% of Python3 online submissions for Student Attendance Record I.
#Memory Usage: 14 MB, less than 11.11% of Python3 online submissions for Student Attendance Record I.
#Fu-Ti, Hsu 
#shifty049@gmail.com
