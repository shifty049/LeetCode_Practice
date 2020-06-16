class Solution:
    def titleToNumber(self, s: str) -> int:
        ix=0
        sumer=0
        while ix<len(s):
            sumer+=(ord(s[::-1][ix])-ord('A')+1)*26**ix
            ix+=1
        return sumer
#Runtime: 24 ms, faster than 95.80% of Python3 online submissions for Excel Sheet Column Number.
#Memory Usage: 13.9 MB, less than 38.85% of Python3 online submissions for Excel Sheet Column Number.
#Fu-Ti, Hsu 
#shifty049@gmail.com