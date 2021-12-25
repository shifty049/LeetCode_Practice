class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
             
        dic = {}
        
        for a, b, c in times:
            
            if a - 1 not in dic:
                dic[a - 1] = {}
            
            dic[a - 1][b - 1] = c
        
        ans = [float(inf) for _ in range(n)]
        
        ans[k - 1] = 0
        
        done = set()
        for _ in range(n):
            
            smallest_idx = min([[i, ix] for ix, i in enumerate(ans) if ix not in done])[1]                
            if smallest_idx in dic:
                
                for j in dic[smallest_idx]:

                    if j not in done:
                        ans[j] = min(ans[j], ans[smallest_idx] + dic[smallest_idx][j])
            
            done.add(smallest_idx)
                
        return -1 if float(inf) in ans else max(ans)

#Runtime: 456 ms, faster than 76.71% of Python3 online submissions for Network Delay Time.
#Memory Usage: 16.1 MB, less than 90.14% of Python3 online submissions for Network Delay Time.
#Fu-Ti, Hsu 
#shifty049@gmail.com
