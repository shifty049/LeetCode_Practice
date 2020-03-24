class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        dic={}
        l=[]
        for i in nums:
            if i not in dic.keys():
                dic[i]=i
                
            else:
                dic[i]+=1
                # record for elements showing twice
                l.append(i)
                
                
        return l

#Runtime: 372 ms, faster than 87.47% of Python3 online submissions for Find All Duplicates in an Array.
#Memory Usage: 21.3 MB, less than 7.14% of Python3 online submissions for Find All Duplicates in an Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com
                