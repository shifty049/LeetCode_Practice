class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        s={}
        for ix,i in enumerate(order):
            s[i]=ix               
        check=True  
        for i in range(len(words)-1):
            
            miner=min(len(words[i]),len(words[i+1]))
            
            for j in range(miner):
                
                if s[words[i][j]]>s[words[i+1][j]]:
                    return False
                elif s[words[i][j]]==s[words[i+1][j]]:
                    pass
                else:
                    break
                if j==miner-1 and len(words[i])>len(words[i+1]):
                    return False
        return check

#Runtime: 32 ms, faster than 86.16% of Python3 online submissions for Verifying an Alien Dictionary.
#Memory Usage: 13.8 MB, less than 69.99% of Python3 online submissions for Verifying an Alien Dictionary.
#Fu-Ti, Hsu 
#shifty049@gmail.com