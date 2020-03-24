class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        days=0
        dayofmonth = [31,28,31,30,31,30,31,31,30,31,30,31]
        weekday=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        year_start=1971
        while year_start<year:
            
            
            if year_start%4==0:
                days+=366
            else:
                days+=365
            
            year_start+=1
                
        
        month_start=1
        while month_start<month:
            if month_start-1==1 and year_start%4==0:            
                days+=dayofmonth[month_start-1]+1
            else:
                days+=dayofmonth[month_start-1]
            
            month_start+=1
        
        days+=day
        return weekday[(days+4)%7]
            
#Runtime: 24 ms, faster than 83.09% of Python3 online submissions for Day of the Week.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Day of the Week.
#Fu-Ti, Hsu 
#shifty049@gmail.com