import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        dic = collections.defaultdict(int)
        mx = 0
        st = 0
        
        for idx, char in enumerate(s):
            dic[char] += 1
            
            if dic[char] > 1:
                
                while s[st] != char:
                    dic[s[st]] -= 1
                    st+= 1
                
                st += 1
                dic[char] -= 1
            
            mx = max((idx - st) + 1, mx)
        
        return mx

#Runtime: 93 ms, faster than 55.67% of Python3 online submissions for Longest Substring Without Repeating Characters.
#Memory Usage: 14.1 MB, less than 50.39% of Python3 online submissions for Longest Substring Without Repeating Characters.
#Fu-Ti, Hsu 
#shifty049@gmail.com