class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        dic={'R':0,'L':0,'U':0,'D':0}
        for i in moves:          
            dic[i]+=1
        
        return dic['R']==dic['L'] and dic['U']==dic['D']

#Runtime: 44 ms, faster than 76.67% of Python3 online submissions for Robot Return to Origin.
#Memory Usage: 13.1 MB, less than 86.21% of Python3 online submissions for Robot Return to Origin.
#Fu-Ti, Hsu 
#shifty049@gmail.com
