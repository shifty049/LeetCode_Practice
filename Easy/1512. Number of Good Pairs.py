class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        dic ={}
        for i in nums:
            
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        
        pair = 0
        for i in dic:
            
            if dic[i]>1:
                pair += dic[i]*(dic[i]-1)//2
        
        return pair

#Runtime: 28 ms, faster than 90.01% of Python3 online submissions for Number of Good Pairs.
#Memory Usage: 14.1 MB, less than 5.24% of Python3 online submissions for Number of Good Pairs.
#Fu-Ti, Hsu 
#shifty049@gmail.com