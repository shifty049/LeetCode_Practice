class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        k=[]
        for ix,i in enumerate(words):
            for jx in range(ix+1,len(words)):
                
                if i in words[jx]:
                    k.append(i)
                if words[jx] in i:
                    k.append(words[jx])
        return list(set(k))
#Runtime: 32 ms, faster than 92.43% of Python3 online submissions for String Matching in an Array.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for String Matching in an Array.
#Fu-Ti, Hsu 
#shifty049@gmail.com