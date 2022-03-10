class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(s, l, r):
            
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l + 1: r]
        ans = ''
        
        for i in range(len(s)):
            
            res =  helper(s, i, i) 
            if len(res) > len(ans):
                ans = res
            
            res =  helper(s, i, i + 1) 
            if len(res) > len(ans):
                ans = res
        
        return ans

#Runtime: 1224 ms, faster than 63.68% of Python3 online submissions for Longest Palindromic Substring.
#Memory Usage: 14 MB, less than 56.77% of Python3 online submissions for Longest Palindromic Substring.
#Fu-Ti, Hsu 
#shifty049@gmail.com