class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
             
        dic = {}
        ans = set()
        for ix,i in enumerate(s[:-9]):
            
            if s[ix:ix+10] not in dic:
                dic[s[ix:ix+10]] = True
            
            else:
                ans.add(s[ix:ix+10])
        
        return list(ans)

#Runtime: 64 ms, faster than 71.17% of Python3 online submissions for Repeated DNA Sequences.
#Memory Usage: 27.9 MB, less than 9.26% of Python3 online submissions for Repeated DNA Sequences.
#Fu-Ti, Hsu 
#shifty049@gmail.com