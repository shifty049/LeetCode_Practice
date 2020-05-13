class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        dic={}
        for i in A:
            if i not in dic:
                dic[i]=1
            # only one element which shows more than once 
            else:             
                return i
#Runtime: 208 ms, faster than 95.10% of Python3 online submissions for N-Repeated Element in Size 2N Array.
#Memory Usage: 15 MB, less than 6.12% of Python3 online submissions for N-Repeated Element in Size 2N Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com