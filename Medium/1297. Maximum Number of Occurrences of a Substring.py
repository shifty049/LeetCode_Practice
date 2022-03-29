class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        dic = {}
        ans = {}
        queue = collections.deque()     
        cnt = 0
        for i in s:
            cnt += 1
            
            queue.append(i)
            
            if i not in dic:
                dic[i] = 1
            
            else:
                dic[i] += 1
            
            if minSize == cnt:
                
                if len(dic) <= maxLetters:
                    check = ''.join(queue)
                    
                    if check not in ans:
                        ans[check] = 1
                    else:
                        ans[check] += 1
                
                cnt -= 1
                rv = queue.popleft()
                dic[rv] -= 1
                
                if not dic[rv]:
                    del dic[rv]
                    
        return max(ans.values()) if ans else 0

#Runtime: 211 ms, faster than 71.40% of Python3 online submissions for Maximum Number of Occurrences of a Substring.
#Memory Usage: 16.2 MB, less than 77.80% of Python3 online submissions for Maximum Number of Occurrences of a Substring.
#Fu-Ti, Hsu 
#shifty049@gmail.com