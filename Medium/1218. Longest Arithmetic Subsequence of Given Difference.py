class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
         
        dic = {}
        
        for i in arr:
          
            dic[i] = 1
            
            if i - difference in dic:
                dic[i] += dic[i - difference]
        
        return max(dic.values())

#Runtime: 540 ms, faster than 75.74% of Python3 online submissions for Longest Arithmetic Subsequence of Given Difference.
#Memory Usage: 28 MB, less than 19.36% of Python3 online submissions for Longest Arithmetic Subsequence of Given Difference.
#Fu-Ti, Hsu 
#shifty049@gmail.com