class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        
        lines=0
        ix=0
        sumer=0
        while ix<len(S):
            
            if sumer+widths[ord(S[ix])-ord('a')]<=100:
                sumer+=widths[ord(S[ix])-ord('a')]
            else:
                sumer=0
                lines+=1
                sumer+=widths[ord(S[ix])-ord('a')]
            ix+=1
        lines+=1
        return [lines,sumer]
            
#Runtime: 32 ms, faster than 58.63% of Python3 online submissions for Number of Lines To Write String.
#Memory Usage: 14 MB, less than 6.25% of Python3 online submissions for Number of Lines To Write String.
#Fu-Ti, Hsu 
#shifty049@gmail.com