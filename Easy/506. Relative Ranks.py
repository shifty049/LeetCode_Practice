class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:        
        dic={}
        for ix,i in enumerate(sorted(nums)[::-1]):
            
            if ix==0:        
                 dic[i]="Gold Medal"
            elif ix==1:
                 dic[i]="Silver Medal"
            elif ix==2:
                 dic[i]="Bronze Medal"
            else:
                 dic[i]=str(ix+1)
             
        return [dic[j] for j in nums]
#Runtime: 60 ms, faster than 99.46% of Python3 online submissions for Relative Ranks.
#Memory Usage: 14.8 MB, less than 25.00% of Python3 online submissions for Relative Ranks.
#Fu-Ti, Hsu 
#shifty049@gmail.com