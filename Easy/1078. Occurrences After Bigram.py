class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s=text.split(' ')
        w=[]
        ix=0
        while ix<len(s)-2:
            if s[ix:ix+2]==[first,second]:   
                w.append(s[ix+2])
                ix+=2
            else:
                ix+=1
        return w
#Runtime: 20 ms, faster than 97.54% of Python3 online submissions for Occurrences After Bigram.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Occurrences After Bigram.
#Fu-Ti, Hsu 
#shifty049@gmail.com