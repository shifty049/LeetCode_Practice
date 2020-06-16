from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = collections.defaultdict(list)
        
        for ix,i in enumerate(nums):          
            dic[i].append(ix)
            
        maxer=max(list(map(len,dic.values())))
        l=[]
        for key,value in dic.items():
            
            if len(value)==maxer:
                l.append(value[-1]-value[0]+1)
        
        return min(l)
#Runtime: 224 ms, faster than 95.53% of Python3 online submissions for Degree of an Array.
#Memory Usage: 16.2 MB, less than 9.09% of Python3 online submissions for Degree of an Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com