class Solution:
    def reformat(self, s: str) -> str:
        l=[]
        n=[]
        
        for i in s:
            
            if i.isdigit():
                n.append(i)
            else:
                l.append(i)
        
        if abs(len(l)-len(n))>1:
            return ''
        
        elif len(l)>len(n):
            return   ''.join([l[ix]+i for ix,i in enumerate(n)])+l[-1]
        elif  len(l)<len(n):
            return  ''.join([n[ix]+i for ix,i in enumerate(l)])+n[-1]
        else:
            return  ''.join([n[ix]+i for ix,i in enumerate(l)])

#Runtime: 40 ms, faster than 97.11% of Python3 online submissions for Reformat The String.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Reformat The String.
#Fu-Ti, Hsu 
#shifty049@gmail.com