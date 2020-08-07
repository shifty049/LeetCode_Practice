class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        sett=[]
        count=1
        for ix,i in enumerate(S):
            if ix:
                if i=='(':
                    if count:
                        sett.append(S[ix])                        
                    count+=1
                elif i==')':
                    count-=1
                    if count:
                        sett.append(S[ix])                        
        return ''.join(sett)

#Runtime: 28 ms, faster than 98.51% of Python3 online submissions for Remove Outermost Parentheses.
#Memory Usage: 13.7 MB, less than 92.32% of Python3 online submissions for Remove Outermost Parentheses.
#Fu-Ti, Hsu 
#shifty049@gmail.com