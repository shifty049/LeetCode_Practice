class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count=0
        for i in range(len(rating)-2):
            
            for j in range(i+1,len(rating)-1):
                
                if rating[i]==rating[j]:
                    break
                elif rating[i]>rating[j]:
                    trend=False
                else:
                    trend=True
                
                for k in range(j+1,len(rating)):
                    
                    if trend and rating[k]>rating[j]:
                        count+=1
                    elif not trend and rating[k]<rating[j]:
                        count+=1
                    else:
                        pass
        return count

#Runtime: 700 ms, faster than 52.40% of Python3 online submissions for Count Number of Teams.
#Memory Usage: 13.8 MB, less than 64.97% of Python3 online submissions for Count Number of Teams.
#Fu-Ti, Hsu 
#shifty049@gmail.com