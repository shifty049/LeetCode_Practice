class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        dic={i:0 for i in set('balloon')}
        
        for i in text:
            if i in dic:
                if i in ['l','o']:
                    dic[i]+=0.5
                else:
                    dic[i]+=1
        
        return int(min(dic.values())//1)

#Runtime: 28 ms, faster than 86.57% of Python3 online submissions for Maximum Number of Balloons.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Maximum Number of Balloons.
#Fu-Ti, Hsu 
#shifty049@gmail.com