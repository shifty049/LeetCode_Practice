class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        
        dic = {}
        for v in votes:
            
            for jx, j in enumerate(v):
                
                if j not in dic:
                    
                    dic[j] = {ix: 0 for ix in range(len(v))}
                
                dic[j][jx]  -= 1
        
        return ''.join([i[-1] for i in sorted([list(value.values()) + [key] for key , value in dic.items()])])

#Runtime: 76 ms, faster than 81.94% of Python3 online submissions for Rank Teams by Votes.
#Memory Usage: 14.5 MB, less than 82.20% of Python3 online submissions for Rank Teams by Votes.
#Fu-Ti, Hsu 
#shifty049@gmail.com