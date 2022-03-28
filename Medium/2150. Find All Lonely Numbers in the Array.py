class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        dic = {}
        
        for i in nums:
            
            if i not in dic:
                    
                dic[i] = True
            else:
                dic[i] = False
            
            dic[i - 1] = False
            dic[i + 1] = False
                       
        return [i for i in dic if dic[i]]

#Runtime: 1887 ms, faster than 63.23% of Python3 online submissions for Find All Lonely Numbers in the Array.
#Memory Usage: 51.1 MB, less than 5.05% of Python3 online submissions for Find All Lonely Numbers in the Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com