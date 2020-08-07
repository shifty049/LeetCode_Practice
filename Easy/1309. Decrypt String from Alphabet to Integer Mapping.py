import string
class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic={str(ix+1):i for ix,i in enumerate(string.ascii_lowercase)}
        q=''
        ix=0
        while ix<len(s):           
            if ix+2>len(s)-1 or s[ix+2]!='#':
                
                q+=dic[s[ix]] 
                ix+=1
            else:
                q+=dic['%s%s'%(s[ix],s[ix+1])]
                ix+=3
        return q

#Runtime: 28 ms, faster than 79.23% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
#Memory Usage: 13.9 MB, less than 29.32% of Python3 online submissions for Decrypt String from Alphabet to Integer Mapping.
#Fu-Ti, Hsu 
#shifty049@gmail.com