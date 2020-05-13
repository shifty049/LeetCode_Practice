class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        length=0
        l_odd=False
        for i in set(s):
            length+=s.count(i)//2*2
            if not l_odd:
                if s.count(i)%2==1:
                    l_odd=True
            
        
        return length+int(l_odd)

#Runtime: 20 ms, faster than 99.37% of Python3 online submissions for Longest Palindrome.
#Memory Usage: 14 MB, less than 8.33% of Python3 online submissions for Longest Palindrome.
#Fu-Ti, Hsu 
#shifty049@gmail.com
