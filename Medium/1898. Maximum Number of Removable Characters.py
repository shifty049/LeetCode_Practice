class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def helper(s, p, rv):
            
            m = len(s)
            n = len(p)

            i = j = 0

            while i < m and j < n:
                if i not in rv:
                    if s[i] == p[j]:
                        j = j + 1
                i += 1

            return j == n
        
        left = 0
        right = min(len(removable), len(s) - len(p))
        ck = True
        while right - left > 1:
            
            med = (left + right) // 2
        
            sub = set(removable[: med])
            ck = helper(s, p, sub)
            if ck:
                left = med
            else:
                right = med
        
        if not ck:
            return left
        
        if ck:
            return right if helper(s, p, set(removable[: right])) else left

#Runtime: 2644 ms, faster than 89.15% of Python3 online submissions for Maximum Number of Removable Characters.
#Memory Usage: 31.9 MB, less than 18.50% of Python3 online submissions for Maximum Number of Removable Characters.
#Fu-Ti, Hsu 
#shifty049@gmail.com
            
        