class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                 dic[i]+=1
            
            if  dic[i]> len(nums)//2:
                return i

#Runtime: 180 ms, faster than 54.39% of Python3 online submissions for Majority Element.
#Memory Usage: 15.2 MB, less than 7.14% of Python3 online submissions for Majority Element.
#Fu-Ti, Hsu 
#shifty049@gmail.com