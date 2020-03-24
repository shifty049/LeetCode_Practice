class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        
        L=[]
        
        for i in sentence.split(' '):
            q={}
            while True:
                for j in dict:
                    # only replace the match for once if q!={} => stop for recording
                    if j ==i[:len(j)] and q=={}:                    
                            q[j]=j
                            i=j
                            break
                break
            L.append(i)
         return ' '.join(L)

#Runtime: 228 ms, faster than 24.74% of Python3 online submissions for Replace Words.
#Memory Usage: 17.1 MB, less than 70.00% of Python3 online submissions for Replace Words.
#Fu-Ti, Hsu 
#shifty049@gmail.com