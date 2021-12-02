from collections import defaultdict
class Solution:
    def longestAwesome(self, s: str) -> int:
        
        dic = defaultdict(list)
        
        mask = 0
        
        dic[0] = [0]
        
        ans = 0
        
        for idx, w in enumerate(s, 1):
            
            mask ^= 1 << (int(w) - 0)
            
            if dic[mask]:
                
                ans = max(ans, idx - dic[mask][0]) 
            
            for n in range(10):
                
                tmp = mask ^ (1 << n)
                
                if dic[tmp]:
                    
                    ans = max(ans, idx - dic[tmp][0]) 
            
            dic[mask].append(idx)
        
        return ans

#Runtime: 1556 ms, faster than 52.14% of Python3 online submissions for Find Longest Awesome Substring.
#Memory Usage: 18.7 MB, less than 5.13% of Python3 online submissions for Find Longest Awesome Substring.
#Fu-Ti, Hsu 
#shifty049@gmail.com
